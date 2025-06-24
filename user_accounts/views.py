from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordResetConfirmView
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.contrib.messages import info, success
from .models import Player
from .forms import PlayerImageUpdate


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    """
    Overrides the default PasswordResetConfirmView to display
    form validation errors as Django messages.
    """
    def form_invalid(self, form):
        message = "<br>".join(
            error for errors in form.errors.values() for error in errors
        )
        info(self.request, message)
        return self.render_to_response(self.get_context_data(form=form))


def login_handler(request):
    """
    Authenticates a user using submitted username and password.
    On success: logs in the user and redirects to the index page.
    On failure: sets message and redirects to the login form.
    """
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        user = authenticate(
            request,
            username=username,
            password=password
            )

        if user is not None:
            login(request, user)
            success(request, "Logged in as " + user.username + ".")
            return redirect("index")

        info(request, "Login failed. Check your credentials.")
        if "signup" in request.session:
            del request.session["signup"]

        return redirect("login_form")

    else:
        info(request, "Wrong request.")

    return redirect("login_form")


def signup_handler(request):
    """
    Registers a new user if validation passes.
    Stores errors as messages and redirects to login form on failure.
    Deletes 'signup' session flag upon successful registration.
    """
    if request.method == "POST":
        request.session["signup"] = True
        data = request.POST

        username = data.get("username", "")
        password = data.get("password", "")
        confirm_password = data.get("confirm-password", "")
        email = data.get("email", "")

        if (Player.objects.filter(username=username).exists()):
            message = "Username already taken :("

        elif not (3 <= len(username) <= 15):
            message = "Username should be between 3 and 15 characters long."

        elif password != confirm_password:
            message = "Passwords do not match."

        else:
            try:
                validate_password(password)
            except ValidationError as e:
                message = "<br>".join(
                    err for error in e.error_list for err in error.messages
                    )
            else:
                Player.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )

                del request.session["signup"]
                success(request, "Sign up completed. You can now log in.")
                return redirect("login_form")

        info(request, message)
        return redirect("login_form")

    else:
        info(request, "Wrong request.")

    return redirect("login_form")


def logout_handler(request):
    """
    Logs out the current user and redirects to the index page.
    Displays a success message if the user was logged in.
    """
    if request.user.is_authenticated:
        logout(request)
        success(request, "You are now logged out.")
    else:
        info(request, "Not logged in.")

    return redirect("index")


def show_personal_profile(request, slg):
    """
    Displays and allows editing of the authenticated user's own profile.
    If accessed via POST, updates personal data and profile image.
    Requires the slug to match the logged-in user's username.
    """
    if request.user.is_anonymous:
        return anon_user(request)

    player = check_player(slg)

    if (
        player is not None
        and request.user.id == player.id
        and request.user.is_authenticated
       ):

        if request.method == "POST":
            data = request.POST
            player.first_name = data.get("first_name", "")
            player.last_name = data.get("last_name", "")
            player.email = data.get("email", "")
            player.birthdate = data.get("birthdate", "")

            # image works through form
            image_form = PlayerImageUpdate(
                data,
                request.FILES,
                instance=player
                )

            if image_form.is_valid():
                image_form.save()
                player.save()
                success(request, "Changes saved successfully.")
            else:
                message = " ".join(
                    err for errors in image_form.errors.values()
                    for err in errors
                )
                info(request, message)

            return redirect("my_profile", player)

        # on GET request
        votes = player.star_rating["votes"]
        if votes:
            rating = player.star_rating["total"] / votes
        else:
            rating = 0

        img_upload = PlayerImageUpdate(use_required_attribute=False)

        return render(
            request,
            "my-profile.html",
            {
                "player": player,
                "rating": rating,
                "votes": votes,
                "img_upload": img_upload
            }
        )

    info(request, "Not authorized.")
    return redirect("index")


def show_profile(request, slg):
    """
    Displays a public user's profile by slug (username).
    If the user does not exist, redirects to the index with a message.
    Currently low on priority list for development.
    """
    player = check_player(slg)

    if player is not None:
        return render(
            request,
            "user-profile.html",
            {"player": player}
        )

    info(request, "User does not exist.")
    return redirect("index")


def login_form(request):
    """
    Renders the login/signup form page.
    """
    return render(
        request,
        "login-forms.html"
    )


# helper functions
def check_player(slg):
    """
    Attempts to retrieve a Player by username (slug).

    Args:
        slg (str): Username slug to look up.

    Returns:
        Player instance if found, None otherwise.
    """
    try:
        player = Player.objects.get(username=slg)
    except Player.DoesNotExist:
        player = None
    return player


def anon_user(request):
    info(request, "You must be logged in for that.")
    return redirect("login_form")
