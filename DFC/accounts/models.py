from django import forms
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    created = models.DateTimeField()
    last_login = models.DateTimeField()
    birthday = models.DateField()
    sex = models.CharField(max_length=10)
    telephone = models.CharField(max_length=11)
    qq = models.CharField(max_length=20)
    description = models.TextField()


class ProfileForm(forms.Form):
    user_profile = forms.modelform_defines_fields(UserProfile)