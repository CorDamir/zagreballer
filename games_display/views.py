from django.shortcuts import render
from django.http import HttpResponse
from .models import FutsalGame, FutsalField


# Create your views here.
def display_games(request):
    joinable_games = FutsalGame.objects.all()
    return render(request, "display.html", {"games": joinable_games})
