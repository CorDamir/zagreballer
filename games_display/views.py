from django.shortcuts import render
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
    new_game_form = CreateGameForm

    return render(
        request,
        "create-game.html",
        {"form": new_game_form}
    )
