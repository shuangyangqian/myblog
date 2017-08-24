# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "users/index.html")


def register(request):
    return render(request, "users/register.html")
