from django.db import models
from django.contrib.auth.models import AbstractUser


class  User(AbstractUser):
    phone = models.CharField(max_length=13)
    work = models.CharField()
    image = models.ImageField(upload_to='media/userimages/')
    youtube = models.CharField()
    intagram = models.CharField()
    facebook = models.CharField()

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
    description = models.TextField(max_length=60)
    image = models.ImageField(upload_to='media/portfolio/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='media/about/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
