from django.db import models
from django.contrib.auth.models import User


class Secy(models.Model):
    club = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class RestaurantManager(models.Model):
    rest = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


# class EventPoster(models.Model):
#     event = models.CharField(max_length=50)
#     user = models.ManyToManyField(User)
