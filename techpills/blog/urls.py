# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^blog/?$', views.blog, name = 'blog'),
	url(r'^blog/(?P<pagenum>[0-9]+)/?$', views.blogpage, name = 'blog'),
	url(r'^blog/article/(?P<articleid>[0-9]+)/?$', views.article, name = 'article'),
]
