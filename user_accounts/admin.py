from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import PlayerCreationForm, PlayerChangeForm
from .models import Player


# Register your models here.
class PlayerAdmin(UserAdmin):
    add_form = PlayerCreationForm
    form = PlayerChangeForm
    model = Player
    list_display = ["email", "username",]


admin.site.register(Player, PlayerAdmin)
