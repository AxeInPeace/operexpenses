# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^registration/$', views.auth_registration, name='registration'),
	url(r'^login/$', views.auth_login, name='login'),
	url(r'^logout/$', views.auth_logout, name='logout'),
]