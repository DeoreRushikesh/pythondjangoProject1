from django.db import models


# Create your models here.
class Artwork(models.Model):
    name = models.CharField(max_length=100)
    artworkstyle = models.CharField(max_length=100)
    price = models.FloatField()
    deliveryCharges = models.FloatField()
    imagePath = models.CharField(max_length=1000, default="")
    description = models.TextField(blank=True)
