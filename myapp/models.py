from django.db import models

# Create your models here.

class Account(models.Model):
    name = models.CharField(max_length=10)
    phone = models.CharField(max_length=20,default='')
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=20)

class Reservation(models.Model):
    day = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    seat = models.CharField(max_length=20)
    ex_name = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    user_phone = models.CharField(max_length=20)
