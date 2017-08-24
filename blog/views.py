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
    return render(request, 'article_page.html', {"article": article})


def article_edit(request, article_id):
    if str(article_id) == '0':
        return render(request, 'edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'edit_page.html', {"article": article})


def edit_action(request):
    title = request.POST["title"]
    content = request.POST["content"]
    article_id = request.POST.get("article_id", '0')

    if article_id == "0":
        models.Article.objects.create(title=title, content=content)
        articles = models.Article.objects.all()
        return render(request, "index.html", {"articles": articles})
    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()

    return render(request, 'article_page.html', {"article": article})
