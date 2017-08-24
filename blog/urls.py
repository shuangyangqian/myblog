from django.conf.urls import url

import views


urlpatterns = [
    url(r'^index/$', views.index, name='index_page'),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
    url(r'^edit/(?P<article_id>[0-9]+)$', views.article_edit, name="article_edit"),
    url(r'^edit/action$', views.edit_action, name="edit_action"),
]