from django.shortcuts import render, redirect
import datetime as dt
from django.contrib.messages import info, success
from .models import FutsalGame
from .forms import CreateGameForm
from user_accounts.views import check_player


def display_games(request):
    all_games = FutsalGame.objects.all().order_by("play_time_start")
    set_games_for_display(all_games)

    after_filters = all_games

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
        info("Cant find this game.")
        return redirect("my_games")

    set_games_for_display(game)

    players = game.all_joining_players.all()

    return render(
        request,
        "game-info.html",
        {
            "game": game,
            "players": players
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


#               --- HELPER FUNCTIONS ---

def set_games_for_display(all_games):
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


def anon_user(request):
    info(request, "You must be logged in for that.")
    return redirect("login_form")
