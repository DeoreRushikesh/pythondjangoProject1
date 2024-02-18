from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    userType = models.CharField(max_length=20, default='')
    first_name = models.CharField(max_length=30)  # Add this line for first name
    last_name = models.CharField(max_length=30)
