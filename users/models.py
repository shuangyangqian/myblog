# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Users(models.Model):
    username = models.CharField(max_length=24, default="username")
    password = models.CharField(max_length=16, default="passw0rd")
    email = models.EmailField()

    def __unicode__(self):
        return self.username