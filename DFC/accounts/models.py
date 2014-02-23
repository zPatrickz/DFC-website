from django import forms
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('A', 'Alien'),
    )
    user = models.OneToOneField(User, unique=True, verbose_name="User", primary_key=True)
    gender = models.CharField(max_length=1, null=True, choices=GENDER)
    birth_date = models.DateField(null=True)
    phone = models.CharField(max_length=20, null=True)
    description = models.TextField(max_length=140, null=True)