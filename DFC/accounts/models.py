# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


GENDER = (
    ('M', '男'),
    ('F', '女'),
    ('A', '女博士'),
)


class UserProfile(models.Model):

    user = models.OneToOneField(User, unique=True, verbose_name="用户", primary_key=True)
    true_name = models.CharField(max_length=20, null=True, verbose_name='真实姓名')
    gender = models.CharField(max_length=1, null=True, choices=GENDER)
    college = models.CharField(max_length=40, null=True, verbose_name='学校')
    birth_date = models.DateField(null=True, verbose_name='出生日期')
    phone = models.CharField(max_length=11, null=True, verbose_name='手机号码')
    qq = models.CharField(max_length=11, null=True, verbose_name='QQ号码')
    description = models.TextField(max_length=140, blank=True, null=True, verbose_name='个性签名')


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])