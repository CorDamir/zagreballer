from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def display_games(request):
    return HttpResponse("Am I working?")
