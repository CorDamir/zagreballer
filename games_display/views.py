from django.shortcuts import render, redirect
import datetime as dt
from django.contrib.messages import info, success
from .models import FutsalGame, CommentModel
from .forms import CreateGameForm, CommentForm
from user_accounts.views import check_player, anon_user


def display_games(request):
    # show only games starting in future
    after_filters = (
        FutsalGame.objects.all()
        .filter(play_time_start__gte=dt.datetime.now())
        .order_by("play_time_start")
        )

    # show only games not created by current user
    usr = check_player(request.user)
    if usr is not None:
        after_filters = after_filters.exclude(creator=usr)

    set_games_for_display(after_filters)

    return render(
        request,
        "display.html",
        {"games": after_filters}
    )


def create_game(request):
    if request.user.is_anonymous:
        return anon_user(request)

    if request.method == "POST":
        data = request.POST

        date = dt.datetime.strptime(data["start_date"], '%Y-%m-%d')
        time = dt.datetime.strptime(
            data["start_hours"] + data["start_minutes"], '%H%M'
            ).time()

        data.play_time_start = dt.datetime.combine(date, time)

        duration = dt.timedelta(
            hours=int(data["duration_hours"]),
            minutes=int(data["duration_minutes"])
            )

        data.play_time_end = data.play_time_start + duration

        saving_form = CreateGameForm(data=data)
        if saving_form.is_valid():
            game = saving_form.save(commit=False)
            game.play_time_start = data.play_time_start
            game.play_time_end = data.play_time_end
            game.creator = request.user
            game.save()

            success(request, "Game successfully created.")
            return redirect(f"../game-info/{game.id}")

        else:
            info(request, "Unable to create game.")
            return redirect("my_games")

    new_game_form = CreateGameForm

    return render(
        request,
        "create-game.html",
        {"form": new_game_form}
    )


def game_info(request, id):
    game = check_game(id)

    if game is None:
        info(request, "Cant find this game.")
        return redirect("my_games")

    set_games_for_display(game)

    players = game.all_joining_players.all()
    comment_form = CommentForm
    # comment_form.root_game = game

    return render(
        request,
        "game-info.html",
        {
            "game": game,
            "players": players,
            "comment_form": comment_form,
        }
    )


def my_games(request):
    if request.user.is_anonymous:
        return anon_user(request)

    created_games = request.user.game_creator.all()
    joined_games = FutsalGame.objects.filter(all_joining_players=request.user)

    set_games_for_display(created_games)
    set_games_for_display(joined_games)

    return render(
        request,
        "my-games.html",
        {
            "created": created_games,
            "joined": joined_games
        }
    )


def join_game(request, id):
    game = check_game(id)
    usr = check_player(request.user)

    if request.user.is_anonymous:
        return anon_user(request)

    if usr is None:
        info(request, "Error with user")
        return redirect("login_form")

    if game is None:
        info(request, "Can't find this game.")
        return redirect("my_games")

    if usr in game.all_joining_players.all():
        message = "Already joined this game."

    elif game.creator == usr:
        message = "Trying to join game you created."

    elif (game.all_joining_players.count() >= game.players_missing):
        message = "Game is already full :( "

    else:
        game.all_joining_players.add(usr)
        success(request, "Successfully joined.")
        return redirect(f"../game-info/{id}")

    info(request, message)
    return redirect("my_games")


def delete_game(request, id):
    game = check_game(id)

    if game is None:
        info(request, "Can't find this game.")
        return redirect("my_games")

    if game.creator == request.user:
        game.delete()
        success(request, "Game deleted.")
        return redirect("my_games")

    info(request, "Can't delete other creators games.")
    return redirect("my_games")


def leave_game(request, id):
    usr = check_player(request.user)
    game = check_game(id)

    if request.user.is_anonymous:
        return anon_user(request)

    if usr is None:
        info(request, "Error with user")
        return redirect("login_form")

    if game is None:
        info(request, "Can't find this game.")
        return redirect("my_games")

    if game.all_joining_players.contains(usr):
        game.all_joining_players.remove(usr)
        success(request, "You left this game.")

    else:
        info(request, "Trying to leave game you're not in.")

    return redirect(f"../game-info/{id}")


def edit_game(request, id):
    game = check_game(id)

    if game is None:
        info(request, "Can't find this game.")
        return redirect("my_games")

    if request.user.is_anonymous:
        return anon_user(request)

    if game.creator.id == request.user.id:
        if request.method == "POST":
            data = request.POST

            date = dt.datetime.strptime(data["start_date"], '%Y-%m-%d')
            time = dt.datetime.strptime(
                data["start_hours"] + data["start_minutes"], '%H%M'
                ).time()

            data.play_time_start = dt.datetime.combine(date, time)

            duration = dt.timedelta(
                hours=int(data["duration_hours"]),
                minutes=int(data["duration_minutes"])
                )

            data.play_time_end = data.play_time_start + duration

            saving_form = CreateGameForm(data=data, instance=game)

            if saving_form.is_valid():
                game = saving_form.save(commit=False)
                game.play_time_start = data.play_time_start
                game.play_time_end = data.play_time_end
                game.save()

                success(request, "Changes saved.")
                return redirect(f"../game-info/{id}")

        else:
            edit_game_form = CreateGameForm(instance=game)

            return render(
                request,
                "create-game.html",
                {"form": edit_game_form}
            )

    else:
        info(request, "Can't edit games you didn't create")
        return redirect("my_games")


def add_comment(request):
    if request.method == "POST":
        data = request.POST
        usr = check_player(request.user.username)

        if usr is None:
            info(request, "Error with user")
            return redirect("login_form")

        comment_form = CommentForm(data=data)

        if comment_form.is_valid:
            saver = comment_form.save(commit=False)
            saver.save()
            return redirect(
                f"../game-info/{data["root_game"]}"
                )

    info(request, "Bad request.")
    return redirect("my_games")


def remove_comment(request, id):
    usr = check_player(request.user.username)

    if usr is None:
        info(request, "You must be logged in.")
        return redirect("login-form")

    try:
        comment = CommentModel.objects.get(id=id)
    except CommentModel.DoesNotExist:
        info(request, "Can't find that comment")
        return redirect("my_games")

    ref = comment.root_game.id

    comment.delete()
    return redirect(f"../game-info/{ref}")


#               --- HELPER FUNCTIONS ---

def set_games_for_display(all_games):
    if type(all_games) is FutsalGame:
        all_games.players_missing = (
            all_games.players_missing - all_games.all_joining_players.count()
            )

    else:
        for game in all_games:
            game.players_missing = (
                game.players_missing - game.all_joining_players.count()
                )


def check_game(id):
    """
    argument: username;
    returns 'Player' model instance if username exists in databese
    returns 'None' otherwise
    """
    try:
        game = FutsalGame.objects.get(id=id)
    except FutsalGame.DoesNotExist:
        game = None
    return game
