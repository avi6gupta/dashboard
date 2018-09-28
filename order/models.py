from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Option(models.Model):
    option = models.CharField(max_length=50)

    def __str__(self):
        return self.option


class MenuObj(models.Model):
    restaurant = models.OneToOneField(Restaurant, primary_key=True, on_delete=models.CASCADE)
    options = models.ManyToManyField(Option)


class OrderList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.CharField(max_length=3000)
