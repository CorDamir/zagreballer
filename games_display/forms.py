from django import forms
from . import models


class CreateGameForm(forms.ModelForm):
    class Meta:
        model = models.FutsalGame
        fields = [
            'futsal_field',
            'players_full',
            'players_missing',
            'age_min',
            'age_max',
            'custom_description'
            ]

    players_nr = [tuple([i, i]) for i in range(6, 31)]
    players_miss = [tuple([i, i]) for i in range(1, 31)]

    players_full = forms.IntegerField(
        widget=forms.Select(choices=players_nr),
        initial=12
        )
    players_missing = forms.IntegerField(
        widget=forms.Select(choices=players_miss),
        initial=3
        )

    age_nr = [tuple([i, i]) for i in range(5, 100)]

    age_min = forms.IntegerField(widget=forms.Select(choices=age_nr))
    age_max = forms.IntegerField(
        widget=forms.Select(choices=age_nr),
        initial=99
        )

    hrs = [tuple([i, i]) for i in range(8, 24)]
    start_hours = forms.IntegerField(
        widget=forms.Select(choices=hrs),
        initial=18
        )

    mins = [list([i, i]) for i in range(0, 51, 10)]
    mins[0][1] = "00"
    start_minutes = forms.IntegerField(widget=forms.Select(choices=mins))

    custom_description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Enter any additional information',
                }
            )
        )

    hrs = [tuple([i, "0" + str(i)]) for i in range(1, 5)]
    duration_hours = forms.IntegerField(
        widget=forms.Select(choices=hrs),
        initial=1
    )

    duration_minutes = forms.IntegerField(
        widget=forms.Select(choices=mins)
    )
