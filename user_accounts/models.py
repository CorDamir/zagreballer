from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField


# Create your models here.
class Player(AbstractUser):
    birthdate = models.DateField()

    def returnDictionary():
        return dict(total=0, votes=0)

    star_rating = models.JSONField(default=returnDictionary)
    image = CloudinaryField("image")

    def __str__(self):
        return self.username
