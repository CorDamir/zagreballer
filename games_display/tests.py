from django.test import TestCase
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import FutsalField, FutsalGame
import datetime as dt

User = get_user_model()

class FutsalFieldModelTests(TestCase):
    def test_create_futsal_field(self):
        field = FutsalField.objects.create(
            name="Central Park Court",
            location_address="123 Main St, City",
            number_of_fields=2,
            location_cityblock=1
        )
        self.assertEqual(field.name, "Central Park Court")
        self.assertEqual(field.location_address, "123 Main St, City")
        self.assertEqual(field.number_of_fields, 2)
        self.assertEqual(field.get_location_cityblock_display(), "Medveščak")
        
    def test_location_gps_default(self):
        field = FutsalField.objects.create(
            name="Test Court",
            location_address="456 Elm St, City",
            location_cityblock=5
        )
        self.assertEqual(field.location_gps, {"longitude": 0, "latitude": 0})


class FutsalGameModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.field = FutsalField.objects.create(
            name="Test Field",
            location_address="789 Pine St, City",
            location_cityblock=3
        )

    def test_create_futsal_game(self):
        game = FutsalGame.objects.create(
            players_full=10,
            players_missing=5,
            custom_description="Friendly match for fun.",
            age_min=18,
            age_max=40,
            play_time_start=dt.datetime(2025, 3, 10, 18, 0),
            play_time_end=dt.datetime(2025, 3, 10, 19, 0),
            creator=self.user,
            futsal_field=self.field
        )
        self.assertEqual(game.players_full, 10)
        self.assertEqual(game.players_missing, 5)
        self.assertEqual(game.custom_description, "Friendly match for fun.")
        self.assertEqual(game.age_min, 18)
        self.assertEqual(game.age_max, 40)
        self.assertEqual(game.creator, self.user)
        self.assertEqual(game.futsal_field, self.field)


class FutsalGameViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")
        self.field = FutsalField.objects.create(
            name="Test Field",
            location_address="789 Pine St, City",
            location_cityblock=3
        )
        self.game = FutsalGame.objects.create(
            players_full=10,
            players_missing=5,
            custom_description="Friendly match for fun.",
            age_min=18,
            age_max=40,
            play_time_start=dt.datetime(2025, 3, 10, 18, 0),
            play_time_end=dt.datetime(2025, 3, 10, 19, 0),
            creator=self.user,
            futsal_field=self.field
        )
    
    def test_display_games_view(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "display.html")

    def test_my_games_view(self):
        response = self.client.get(reverse("my_games"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "my-games.html")

    def test_game_info_view(self):
        response = self.client.get(reverse("game_info", args=[self.game.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "game-info.html")

