# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid
# Create your models here.
class UserModel(models.Model):
    Email = models.EmailField()
    Name = models.CharField(max_length=255)
    Username = models.CharField(max_length=128)
    Password = models.CharField(max_length=40)
    created_on = models.DateTimeField(auto_now_add = True)
    Updated_on = models.DateTimeField(auto_now=True)


#here the code to create a session
class SessionToken(models.Model):
        user = models.ForeignKey(UserModel)
        session_token = models.CharField(max_length=255)
        last_request_on = models.DateTimeField(auto_now=True)
        created_on = models.DateTimeField(auto_now_add=True)
        is_valid = models.BooleanField(default=True)

        def create_token(self):
            self.session_token = uuid.uuid4()
