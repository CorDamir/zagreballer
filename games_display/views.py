from django.shortcuts import render, redirect
import datetime as dt
from user_accounts.views import del_msg
from .models import FutsalGame
from .forms import CreateGameForm


# Create your views here.
def display_games(request):
    joinable_games = FutsalGame.objects.all().order_by("play_time_start")

    return render(
        request,
        "display.html",
        {"games": joinable_games}
    )


def create_game(request):
    del_msg(request)

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

        print(data.play_time_end)
        print(type(data.play_time_end))

        saving_form = CreateGameForm(data=data)
        if saving_form.is_valid():
            game = saving_form.save(commit=False)
            game.play_time_start = data.play_time_start
            game.play_time_end = data.play_time_end
            game.creator = request.user
            game.save()

            request.session["message"] = "Game successfully created."
            request.session["success"] = True
            return redirect("index")

    new_game_form = CreateGameForm

    return render(
        request,
        "create-game.html",
        {"form": new_game_form}
    )


def game_info(request, slg):
    del_msg(request)

    game = FutsalGame.objects.filter(id=slg).first()
    players = game.all_joining_players.all()
    duration = game.play_time_end - game.play_time_start
    hs = duration.seconds // 3600
    mins = duration.seconds // 60 % 60

    players_missing = game.players_missing - players.count()
    game.players_full = game.players_full // 2

    return render(
        request,
        "game-info.html",
        {
            "game": game,
            "players": players,
            "duration": duration,
            "players_missing": players_missing,
            "hs": hs,
            "mins": mins
        }
    )


def my_games(request):
    del_msg(request)

    created_games = request.user.game_creator.all()
    joined_games = FutsalGame.objects.filter(all_joining_players=request.user)

    return render(
        request,
        "my-games.html",
        {
            "created": created_games,
            "joined": joined_games
        }
    )


def join_game(request, id):
    del_msg(request)

    game = FutsalGame.objects.get(id=id)
    usr = request.user

    if usr in game.all_joining_players.all():
        message = "Already joined this game."

    elif game.creator == usr:
        message = "Trying to join game you created."

    elif (game.all_joining_players.count() >= game.players_missing):
        message = "Game is already full :( "

    else:
        game.all_joining_players.add(usr)
        message = "Successfully joined."
        request.session["success"] = True

    request.session["message"] = message

    return render(
        request,
        "my-games.html"
    )


def delete_game(request, id):
    del_msg(request)

    game = FutsalGame.objects.filter(id=id)[0]
    if game.creator == request.user:
        game.delete()
        request.session["message"] = "Game deleted."
        request.session["success"] = True
        return redirect("my_games")

    request.session["message"] = "Can't delete other creators games."
    return redirect("index")
