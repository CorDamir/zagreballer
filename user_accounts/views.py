from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from .models import Player


# views
def login_handler(request):
    if request.method == "POST":
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

        if "signup" in request.session:
            del request.session["signup"]

    else:
        request.session["message"] = "Wrong request."

    return redirect("index")


def signup_handler(request):
    if request.method == "POST":
        request.session["signup"] = True
        data = request.POST
        user = Player

        user.email = data["email"]
        user.username = data["username"]
        user.password = data["password"]

        if (Player.objects.filter(username=user.username).exists()):
            message = "Username already taken :("

        elif len(user.username) < 3 or len(user.username) > 15:
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
        if "signup" in request.session:
            del request.session["signup"]

    else:
        request.session["message"] = "Wrong request."

    return redirect("index")


def logout_handler(request):
    if request.user.is_authenticated:
        logout(request)
        request.session["message"] = "You are now logged out."
    else:
        request.session["message"] = "Not logged in."

    if "signup" in request.session:
        del request.session["signup"]

    return redirect("index")


def show_personal_profile(request, slg):
    player = check_player(slg)

    if (
        player is not None
        and request.user.id == player.id
        and request.user.is_authenticated
         ):
        return render(
            request,
            "my-profile.html",
            {"player": player}
            )


def show_profile(request, slg):
    player = check_player(slg)

    if player is not None:
        return render(
            request,
            "user-profile.html",
            {"player": player}
        )

    request.session["message"] = "User does not exist."
    return redirect("index")


# helper functions
def check_player(slg):
    """
    argument: username;
    returns 'Player' model if username exists in databese
    returns 'None' otherwise
    """
    try:
        player = Player.objects.get(username=slg)
    except Player.DoesNotExist:
        player = None
    return player
