from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_handler, name='login_handler'),
    path('signup', views.signup_handler, name="signup_handler"),
    path('logout', views.logout_handler, name="logout_handler")
]
