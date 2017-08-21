# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from . import models
from django.shortcuts import render

# Create your views here.


def index(request):
    articles = models.Article.objects.all()
    return render(request, 'index.html', {"articles": articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'article_page.html', article)
