from django.db import models
from django.contrib.auth.models import UserManager



class User_data(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    user_name = models.CharField(max_length=128,default='')
    email = models.EmailField(max_length=254,unique=True)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    objects = UserManager()
