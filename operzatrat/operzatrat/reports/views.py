from django.shortcuts import render
from ..inputforms.models import *


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
	sites = {}
	workovertypes = {}
	works = {}
	pathcard_works = WorksOnPathcard.objects.all()
	for item in pathcards:
		sites[item] = [
			item.kkp_site_type,
			item.door_site_type,
			item.ventil_site_type,
			item.eqi_site_type,
			item.eli_site_type,
			item.pipe_site_type,
			item.grb_site_type,
		]
		works[item] = []
		workovertypes[item] = []
		for w in pathcard_works:
			if w.pathcard == item:
				works[w.pathcard].append(w)
				if w.work.owned_to not in workovertypes[w.pathcard]:
					workovertypes[w.pathcard].append(w.work.owned_to)
	context = {
		"pathcards": pathcards,
		"works": works,
		"sites": sites,
		"workovertypes": workovertypes,
	}
	return render(request, 'pathcards.html', context)
