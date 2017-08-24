# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Article
from django.contrib import admin

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "pub_time")
    list_filter = ("pub_time",)

admin.site.register(Article, ArticleAdmin)

