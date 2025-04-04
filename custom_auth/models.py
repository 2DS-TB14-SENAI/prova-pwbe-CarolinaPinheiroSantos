from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=50)
    address = models.TextField()
    birth_date = models.DateField()
    is_verified = models.BooleanField()
