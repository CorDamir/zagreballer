from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_handler, name='login_handler'),
]
