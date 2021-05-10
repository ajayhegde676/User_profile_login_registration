from django.db import models


class User_data(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    user_name = models.CharField(max_length=128,default='')
    email = models.EmailField(max_length=254,unique=True)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
