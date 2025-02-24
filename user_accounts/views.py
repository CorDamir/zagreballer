from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from .models import Player


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
        login(request, user)
        message = "Logged in as " + user.username + "."
    else:
        message = "Login failed. Check your credentials."

    request.session["message"] = message
    return redirect("index")


def signup_handler(request):
    data = request.POST
    user = Player

    user.email = data["email"]
    user.username = data["username"]
    user.password = data["password"]

    if len(user.username) < 3 or len(user.username) > 15:
        message = "Username should be between 3 and 15 characters long."

    elif user.password != data["confirm-password"]:
        message = "Passwords do not match."

    else:
        try:
            validate_password(
                user.password, user=user, password_validators=None
            )

        except ValidationError as e:
            message = ""
            for error in e.error_list:
                for err in error.messages:
                    message += err + "<br>"
        else:
            user = Player.objects.create_user(
                username=user.username,
                email=user.email,
                password=user.password
                )
            message = "Sign up completed. You can now log in."

    request.session["message"] = message
    return redirect("index")
