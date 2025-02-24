from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.
def login_handler(request):
    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(
        request,
        username=username,
        password=password
        )

    if user is not None:
        user = login(request, user)

        messages.add_message(
            request,
            messages.SUCCESS,
            "You are now logged in."
        )
    else:
        messages.add_message(
            request,
            messages.ERROR,
            "Login failed. Check your credentials."
        )

    return request
