# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Users
# Register your models here.


class UsersAdmin(admin.ModelAdmin):
    list_filter = ("username", "email")


admin.site.register(Users, UsersAdmin)
