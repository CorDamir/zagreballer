from django.shortcuts import render
from .models import FutsalGame
from user_accounts.views import login_handler


# Create your views here.
def display_games(request):
    if request.method == "POST":
        request = login_handler(request)

    joinable_games = FutsalGame.objects.all()

    return render(
        request,
        "display.html",
        {
            "games": joinable_games
        }
    )
