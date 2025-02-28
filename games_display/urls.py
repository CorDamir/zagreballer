from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_games, name='index'),
    path('create-game', views.create_game, name="create_game"),
    path('game-info/<slug:slg>', views.game_info, name="game_info"),
    path('my-games', views.my_games, name="my_games"),
    path('join-game/<int:id>', views.join_game, name="join_game"),
    path('delete-game/<int:id>', views.delete_game, name="delete_game")
]
