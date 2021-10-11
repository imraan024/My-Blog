from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from members.models import UserProfile


class Post(models.Model):
    title = models.CharField(max_length= 255)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="author")
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
    USER_CHOICES = (
    ('Admin', 'Admin'),
    ('Editor', 'Editor'),
    ('Member', 'Member'),
    )
    user = models.OneToOneField(UserProfile, null = True, on_delete = models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to = 'images/')
    user_status = models.CharField(max_length=50,choices=USER_CHOICES, null = True, blank= True)
    auth_token = models.CharField(max_length=100, null = False, blank=True)
    is_varified = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.user)
    def get_absolute_url(self):
        return reverse ('home')

