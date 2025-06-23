from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import CustomSetPasswordForm
from .views import CustomPasswordResetConfirmView


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
        name="password_reset_form",
    ),
    path(
        "forgotten-password/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="forgotten-password/reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "forgotten-password/confirm/<uidb64>/<token>/",
        CustomPasswordResetConfirmView.as_view(
            template_name="forgotten-password/reset_confirm.html",
            form_class=CustomSetPasswordForm
        ),
        name="password_reset_confirm",
    ),
    path(
        "forgotten-password/complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="forgotten-password/reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    ]
