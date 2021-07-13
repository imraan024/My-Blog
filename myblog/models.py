from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Post(models.Model):
    title = models.CharField(max_length= 255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    body = models.TextField()
    date = models.DateField(auto_now_add = True) 
    category = models.CharField(max_length= 255)
    post_status = models.IntegerField(default=0)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    def get_absolute_url(self):
        return reverse ('home') 


class Category(models.Model):
    name = models.CharField(max_length= 255)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse ('home')


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to = 'images/')
    user_status = models.CharField(max_length=50, null = True, blank= True)
    def __str__(self):
        return str(self.user)
    def get_absolute_url(self):
        return reverse ('home')

