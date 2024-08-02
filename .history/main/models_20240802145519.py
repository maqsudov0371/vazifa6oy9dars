from django.db import models
from django.contrib.auth.models import AbstractUser, User

class User(AbstractUser):
    phone = models.CharField(max_length=15)  # `PositiveIntegerField` o'rniga `CharField` ishlatiladi
    work = models.CharField(max_length=255)  # `max_length` qo'shildi
    image = models.ImageField(upload_to='media/userimages/')
    youtube = models.CharField(max_length=255)  # `max_length` qo'shildi
    instagram = models.CharField(max_length=255)  # `max_length` qo'shildi
    facebook = models.CharField(max_length=255)  # `max_length` qo'shildi

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='main_user_groups',  # `related_name` qo'shildi
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='main_user_permissions',  # `related_name` qo'shildi
        blank=True
    )

    def __str__(self):
        return self.first_name
    

class Services(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='media/services/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    

class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=60)  # `max_length` `TextField` uchun keraksiz, shuning uchun olib tashlash mumkin
    image = models.ImageField(upload_to='media/portfolio/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='media/about/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    years = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
