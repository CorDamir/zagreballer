from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', views.login_handler, name="login_handler"),
    path('signup', views.signup_handler, name="signup_handler"),
    path('logout', views.logout_handler, name="logout_handler"),
    path('login-form', views.login_form, name="login_form"),
    path(
        '<slug:slg>/edit/',
        views.show_personal_profile,
        name="my_profile"
        ),
    path(
        "forgotten-password/",
        auth_views.PasswordResetView.as_view(
            template_name="forgotten-password/reset_form.html"
        ),
        name="reset_form",
    ),
    path(
        "forgotten-password/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="forgotten-password/reset_done.html"
        ),
        name="reset_done",
    ),
    path(
        "forgotten-password/confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="forgotten-password/reset_confirm.html"
        ),
        name="reset_confirm",
    ),
    path(
        "forgotten-password/complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="forgotten-password/reset_complete.html"
        ),
        name="reset_complete",
    ),
    ]
