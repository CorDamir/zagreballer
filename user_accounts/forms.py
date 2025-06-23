from django import forms
from . import models
from django.core.exceptions import ValidationError


class PlayerImageUpdate(forms.ModelForm):
    class Meta:
        model = models.Player
        fields = ['image']
        labels = {'image': 'Change picture'}

    def clean_image(self):
        file = self.cleaned_data.get('image')
        if file:
            if not file.content_type.startswith('image'):
                raise ValidationError("Uploaded file must be image type.")
        return file
