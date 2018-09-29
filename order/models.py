from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    img = models.ImageField(upload_to="restaurant_images", blank=True)
    description = models.CharField(max_length=50, default=0)

    def __str__(self):
        return self.name


class Option(models.Model):
    option = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.option


class MenuObj(models.Model):
    restaurant = models.OneToOneField(Restaurant, primary_key=True, on_delete=models.CASCADE)
    options = models.ManyToManyField(Option)


class OrderList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.CharField(max_length=3000)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default=0)
