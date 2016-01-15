from django.shortcuts import render
from ..inputforms.models import *
# Create your views here.

def reports_start(request):
	return render(request, 'start_reports.html')

def reports_projects(request):
	projects = Project.objects.all()
	station_types = StationType.objects.all()
	stations = Station.objects.all()

	context = {
		"projects": projects,
		"stations": stations,
		"station_types": station_types,
	}
	return render(request, 'projects.html', context)

def reports_pathcards(request):
	pathcards = Pathcard.objects.all()
	pathcard_works = WorksOnPathcard.objects.all()
	
	context = {
		"pathcards": pathcards,
		"pathcard_works": pathcard_works,
	}

	return render(request, 'pathcards.html', context)