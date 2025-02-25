from django import forms
from . import models


class PlayerImageUpdate(forms.ModelForm):
    class Meta:
        model = models.Player
        fields = ['image']
        labels = {'image': 'Change picture'}
