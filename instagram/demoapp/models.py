# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserModel(models.Model):
    Email = models.EmailField()
    name = models.CharField(max_length=255)
    Username = models.CharField(max_length=128)
    Password = models.CharField(max_length=40)
    created_on = models.DateTimeField(auto_now_add = True)
    Updated_on = models.DateTimeField(auto_now=True)