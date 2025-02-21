from django.db import models
from user_accounts.models import Player


# Create your models here.
class FutsalField(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    location_address = models.TextField(null=False)
    number_of_fields = models.IntegerField(default=1)

    CITYBLOCK_CHOICES = (
        (0, "Donji grad"),
        (1, "Gornji grad – Medveščak"),
        (2, "Trnje"),
        (3, "Maksimir"),
        (4, "Peščenica – Žitnjak"),
        (5, "Novi Zagreb – istok"),
        (6, "Novi Zagreb – zapad"),
        (7, "Trešnjevka – sjever"),
        (8, "Trešnjevka – jug"),
        (9, "Črnomerec"),
        (10, "Gornja Dubrava"),
        (11, "Donja Dubrava"),
        (12, "Stenjevec"),
        (13, "Podsused – Vrapče"),
        (14, "Podsljeme"),
        (15, "Sesvete"),
        (16, "Brezovica")
    )

    location_cityblock = models.IntegerField(
        null=False, choices=CITYBLOCK_CHOICES
        )

    def returnDictionary():
        return dict(longitude=0, latitude=0)

    location_gps = models.JSONField(default=returnDictionary)

    def __str__(self):
        return f"{self.name} | {self.get_location_cityblock_display()}"

    @property
    def get_cityblock(self):
        for i in self.CITYBLOCK_CHOICES:
            if i[0] == int(self.location_cityblock):
                return i[1]
        return self.location_cityblock


class FutsalGame(models.Model):
    players_full = models.IntegerField()
    players_missing = models.IntegerField()
    custom_description = models.TextField()
    age_min = models.IntegerField()
    age_max = models.IntegerField()
    play_time_start = models.DateTimeField()
    play_time_end = models.TimeField()
    field_number = models.IntegerField()

    creator = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="game_creator"
        )

    futsal_field = models.OneToOneField(
        FutsalField, on_delete=models.CASCADE
        )

    all_joining_players = models.ManyToManyField(
        Player, related_name="joining_players"
        )
