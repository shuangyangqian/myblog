from django.conf.urls import url, include
from django.contrib import admin
import views


urlpatterns = [
    url(r'^$', views.index, name="index_page"),
    url(r'^register/$', views.register, name="register_user")
]
