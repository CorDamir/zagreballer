from django import forms
from . import models
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import SetPasswordForm


class PlayerImageUpdate(forms.ModelForm):
    class Meta:
        model = models.Player
        fields = ["image"]
        labels = {"image": "Change picture"}

    def clean_image(self):
        file = self.files.get("image")
        if file:
            if not file.content_type.startswith("image"):
                raise ValidationError("Uploaded file must be image type.")
        return self.cleaned_data.get("image")


class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        (self.fields['new_password1'].widget.attrs
         .update({'placeholder': 'Enter new password'}))

        (self.fields['new_password2'].widget.attrs
         .update({'placeholder': 'Confirm new password'}))
