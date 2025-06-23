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


def format_date_inputs(data):
    """
    accepts POST data from game input form
    returns *False* if date input invalid
    returns dictionary with formatted datetime objects;
    *play_time_start*
    *play_time_end*

    """
    # if user deleted date/part of date on input return None
    try:
        date = dt.datetime.strptime(data["start_date"], '%Y-%m-%d')
        time = dt.datetime.strptime(
            data["start_hours"] + data["start_minutes"], '%H%M'
        ).time()

        play_time_start = dt.datetime.combine(date, time)
        duration = dt.timedelta(
            hours=int(data["duration_hours"]),
            minutes=int(data["duration_minutes"])
            )
        play_time_end = play_time_start + duration
    except (ValueError, TypeError):
        return None

    return {
        "play_time_start": play_time_start,
        "play_time_end": play_time_end
    }


def validate_game_form(request, dates):
    """
    Checks for correct user input for game data,
    sets info message on failed validation.
    returns *FutsalGame model* with correct data and "True" if data valid
    returns *CreateGameForm object* and "False" on invalid data
    """
    data = request.POST
    saving_form = CreateGameForm(data=data)

    # validate date is input
    if dates is None:
        info(request, "Please select a date")

    # validate start time to be at least one hour in future
    elif dates["play_time_start"] < dt.datetime.now() + dt.timedelta(hours=1):
        info(request, "Start time must be at least an hour in advance")

    # validate needed players number (creator not necessarily player)
    elif int(data["players_missing"]) > int(data["players_full"]) * 2:
        info(request, "Needed players can't exceed total players")

    # validate age range entry - max bigger than min
    # difference of 4 includes 5 different ages
    elif int(data["age_max"]) - int(data["age_min"]) < 4:
        info(
            request,
            "Please select ideal age range with at least five "
            "year span and maximum age larger than minimum"
            )

    # ALL OK: return game model and True for validation
    elif saving_form.is_valid():
        game = saving_form.save(commit=False)
        game.play_time_start = dates["play_time_start"]
        game.play_time_end = dates["play_time_end"]
        game.creator = request.user
        return game, True
    else:
        info(request, "Unable to create game.")

    # validation fail: return form with user's inputs and False for validation
    return saving_form, False


def create_game(request):
    if request.user.is_anonymous:
        return anon_user(request)

    if request.method == "POST":
        dates = format_date_inputs(request.POST)
        saving_form, form_validated = validate_game_form(request, dates)

        # if everything is ok save to database and redirect
        if form_validated:
            saving_form.save()
            success(request, "Game successfully created.")
            return redirect(f"../game-info/{saving_form.id}")
        else:
            date_for_form = request.POST.get("start_date", "")

    else:
        saving_form = CreateGameForm
        date_for_form = dt.date.today().isoformat()

    # saving_form will be default one if GET method
    # otherwise show user input and info message
    return render(
        request,
        "create-game.html",
        {
            "form": saving_form,
            "start_date": date_for_form
        }
    )


def game_info(request, id):
    game = check_game(id)

    if game is None:
        info(request, "Cant find this game.")
        return redirect("my_games")

    set_games_for_display(game)

    players = game.all_joining_players.all()
    comment_form = CommentForm

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
            dates = format_date_inputs(request.POST)
            saving_form, form_validated = validate_game_form(request, dates)

            if form_validated:
                # set the instance to edit existing game!
                saving_form.id = game.id
                saving_form.save()
                success(request, "Changes saved.")
                return redirect(f"../game-info/{id}")

        # on GET request or form not validated
        edit_game_form = get_complete_edit_form(game)
        date_for_form = game.play_time_start.date().isoformat()

        return render(
            request,
            "create-game.html",
            {
                "form": edit_game_form,
                "start_date": date_for_form
            }
        )

    else:
        info(request, "Can't edit games you didn't create")
        return redirect("my_games")


def get_complete_edit_form(game):
    """
    receives FutsalGame model,
    calculates start time and duration from datetime objects,
    returns CreateGameForm with complete model instance data
    """
    edit_game_form = CreateGameForm(instance=game)

    total_duration_mins = int(
        (game.play_time_end - game.play_time_start)
        .total_seconds() // 60
        )

    start_hours = game.play_time_start.hour
    start_minutes = game.play_time_start.minute
    duration_hours = total_duration_mins // 60
    duration_minutes = total_duration_mins % 60

    edit_game_form.fields["start_hours"].initial = start_hours
    edit_game_form.fields["start_minutes"].initial = start_minutes
    edit_game_form.fields["duration_hours"].initial = duration_hours
    edit_game_form.fields["duration_minutes"].initial = duration_minutes

    return edit_game_form


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
    returns 'FutsalGame' model instance if given ID exists in databese
    returns 'None' otherwise
    """
    try:
        game = FutsalGame.objects.get(id=id)
    except FutsalGame.DoesNotExist:
        game = None
    return game
