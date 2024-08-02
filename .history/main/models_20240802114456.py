from django.db import models
from django.contrib.auth.models import AbstractUser


class  User(AbstractUser):
    phone = models.CharField(max_length=13)
    work = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/userimages/')
