from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.reports_start, name='reports_start'),
	url(r'^project/$', views.reports_projects, name='reports_projects'),
	url(r'^pathcard/$', views.reports_pathcards, name='reports_pathcard'),
	
]