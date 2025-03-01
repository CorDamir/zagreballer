from django.shortcuts import render, redirect
import datetime as dt
from django.contrib.messages import info, success
from .models import FutsalGame
from .forms import CreateGameForm


# Create your views here.
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
            return redirect("index")

    new_game_form = CreateGameForm

    return render(
        request,
        "create-game.html",
        {"form": new_game_form}
    )


def game_info(request, slg):
    game = FutsalGame.objects.filter(id=slg).first()
    players = game.all_joining_players.all()

    players_missing = game.players_missing - players.count()
    game.players_full = game.players_full // 2

    return render(
        request,
        "game-info.html",
        {
            "game": game,
            "players": players,
            "players_missing": players_missing,
        }
    )


def my_games(request):
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
        success(request, "Successfully joined.")
        return redirect("my_games")

    info(request, message)
    return redirect("my_games")


def delete_game(request, id):
    game = FutsalGame.objects.filter(id=id)[0]
    if game.creator == request.user:
        game.delete()
        success(request, "Game deleted.")
        return redirect("my_games")

    info(request, "Can't delete other creators games.")
    return redirect("my_games")


#               --- HELPER FUNCTIONS ---

def set_games_for_display(all_games):
    for game in all_games:
        game.players_missing = (
            game.players_missing - game.all_joining_players.count()
            )
        game.players_full = game.players_full // 2
