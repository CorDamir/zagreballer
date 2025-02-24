from django import forms
from .models import Player


class PlayerCreationForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ("username", "email")


class PlayerChangeForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ("username", "email")


class LoginForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ("username", "password")
