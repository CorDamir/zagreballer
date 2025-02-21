from django.db import models


# Create your models here.
class FutsalField(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    location_address = models.TextField(null=False)

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
        return f"{self.name} | {self.get_cityblock}"

    @property
    def get_cityblock(self):
        for i in self.CITYBLOCK_CHOICES:
            if i[0] == int(self.location_cityblock):
                return i[1]
        return self.location_cityblock
