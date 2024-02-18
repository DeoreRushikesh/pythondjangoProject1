from django.db import models
from ..artist.models import *


# Create your models here.
class Order(models.Model):
    citizenName = models.CharField(max_length=200,null=False)
    artName = models.CharField(max_length=200)
    contact = models.BigIntegerField()
    address = models.CharField(max_length=500)
    paidAmount = models.FloatField()
