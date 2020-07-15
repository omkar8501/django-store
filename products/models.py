from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.CharField(max_length=2048)
    stock = models.IntegerField()
    price = models.FloatField()
    category = models.CharField(default=0, max_length=255)