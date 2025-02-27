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

    return render(
        request,
        "game-info.html",
        {"game": game}
    )
