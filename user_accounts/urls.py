from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_handler, name="login_handler"),
    path('signup', views.signup_handler, name="signup_handler"),
    path('logout', views.logout_handler, name="logout_handler"),
    path('users/edit/<slug:slg>', views.show_personal_profile,
         name="my_profile"),
    path('users/<slug:slg>', views.show_profile, name="profile"),
]
