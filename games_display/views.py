from django.shortcuts import render, redirect
import datetime as dt
from .models import FutsalGame
from .forms import CreateGameForm


# Create your views here.
def display_games(request):
    joinable_games = FutsalGame.objects.all()
    message = request.session["message"]

    return render(
        request,
        "display.html",
        {
            "games": joinable_games,
            "message": message
        }
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
            return redirect("index")

    new_game_form = CreateGameForm

    return render(
        request,
        "create-game.html",
        {"form": new_game_form}
    )
