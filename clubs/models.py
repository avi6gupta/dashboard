from django.db import models


class Club(models.Model):
    name = models.CharField(max_length=50)


class Post(models.Model):
    text = models.CharField(max_length=500, null=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
