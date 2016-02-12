# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.forms_start, name='forms_start'),
	url(r'^project/$', views.forms_project, name='newproject'),
	url(r'^station/$', views.forms_station, name='newstation'),
	url(r'^chooseproject/$', views.choose_project, name='choose_station'),
	url(r'^pathcard/$', views.forms_pathcard, name='newpathcard'),
	url(r'^order/$', views.forms_order, name='neworder'),
	url(r'^get_time/$', views.get_time, name='get_time'),
	url(r'^get_description/$', views.get_description, name='get_description'),
	url(r'^choosepathcard/$', views.order_choose_pathcard, name='order_choose_pathcard'),
	url(r'^pathcardsfororder/$', views.get_pathcards_for_order, name='get_pathcards_for_order'),

#	url(r'^/station_timespend/$', views.forms_st_timespend, name='station_timespend'),
]
