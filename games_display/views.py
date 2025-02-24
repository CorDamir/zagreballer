from django.shortcuts import render
from .models import FutsalGame


# Create your views here.
def display_games(request):
    joinable_games = FutsalGame.objects.all()
    if "message" in request.session:
        message = request.session["message"]

    return render(
        request,
        "display.html",
        {
            "games": joinable_games,
            "message": message
        }
    )
