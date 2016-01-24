# -*- coding: utf-8 -*-

from django.shortcuts import render
from models import *
from operzatrat.settings import STATICFILES_DIRS
from django.http import HttpResponseRedirect, JsonResponse
from django.template.defaulttags import register

def forms_start(request):
	return render(request, 'startforms.html')


def forms_project(request):
	stations = StationType.objects.all()
	context = {"stations": stations}
	if request.method == "GET":	
		return render(request, 'newproject.html', context)

	if request.method == "POST":
		try:
			project_name = request.POST.get('projectname')
			start_date = request.POST.get('start_date')
			end_date = request.POST.get('end_date')
		except:
			context["warning_message"] = u"Проблемы на сервере, попробуйте ещё раз."
			return render(request, 'newproject.html', context)

		if (project_name == "a"):
			context["warning_message"] = u"Пожалуйста, введите имя проекта"
			return render(request, 'newproject.html', context)

		fields_num = request.POST.get('fields_num')
		if (fields_num == "" or fields_num == "0"):
			context["warning_message"] = u"Ошибка при выборе станции"
			return render(request, 'newproject.html', context)

		station_type = []
		found_station = []

		for i in range(1, int(fields_num) + 1):
			station_type.append(request.POST.get('st_field_' + str(i)))

			try:
				found_station.append(StationType.objects.get(id=station_type[i - 1]))
			except:
				context["warning_message"] = str(i) + u"-я станция не найдена."
				return render(request, 'newproject.html', context)

		if (start_date == "" or end_date == ""):
			newproj = Project.objects.create(name=project_name)
		else:
			newproj = Project.objects.create(name=project_name, start_date=start_date, end_date=end_date)
		
		for i in range(1, int(fields_num) + 1):
			Station.objects.create(project=newproj, station=found_station[i - 1], left_to_card=True)

		context["success_message"] = u"Проект с " + fields_num + u" станциями успешно добавлен"
		return render(request, 'newproject.html', context)


def forms_station(request):
	stations = StationType.objects.all()
	context = {
		"stations": stations,
	}
	
	if request.method == "GET":
		return render(request, 'newstation.html', context)

	if request.method == "POST":
		stationname = request.POST.get('stationname')
		if stationname != None:
			if StationType.objects.filter(name=stationname):
				context["message"] = "Станция с таким названием уже существует"
				return render(request, 'newstation.html', context)
			else:
				StationType.objects.create(name=stationname)
				context["message"] = "Станция добавлена!"
				return render(request, 'newstation.html', context)
		else:
			context["message"] = "Введите название для станции"
			return render(request, 'newstation.html', context)


def choose_project(request):
	
	stations = Station.objects.filter(left_to_card=True)
	projects = []
	for station in stations:
		if station.project not in projects:
			projects.append(station.project)

	context = {
		"projects": projects,
		"stations": stations,
	}

	if request.method == "GET":
		return render(request, 'newpathcard.html', context)


def fill_dict(s):
	d = {}
	for item in s:
		if item.owned_to not in d:
			d[item.owned_to] = []
		d[item.owned_to].append(item)
	return d


def init_worktypes(request):
	wt_amount = int(request.POST.get('wt_amount'))
	custom_wt_amount = int(request.POST.get('custom_wt_amount'))

	returned_value = {
		"work_type": None, 
		"quantity": None,
		"time": None,
	}
	returned_value["work_type"] = []
	returned_value["quantity"] = []
	returned_value["time"] = []
	returned_value["custom_work_type"] = []

	for i in range(wt_amount):
		returned_value["work_type"].append( int( request.POST.get('wt_' + str(i)) ) )
		returned_value["quantity"].append( int( request.POST.get('qnt_' + str(i)) ) )
		returned_value["time"].append( int( request.POST.get('time_' + str(i)) ) )

	for i in range(wt_amount, wt_amount + custom_wt_amount):
		owner_id = request.POST.get('overtype_' + str(i))
		owner = WorkOvertype.objects.get(id=owner_id)
		curwt = WorkType.objects.create(name=request.POST.get('wt_'+ str(i)), custom=True, owned_to=owner)

		returned_value["work_type"].append(curwt.id)
		returned_value["quantity"].append( int( request.POST.get('qnt_' + str(i)) ) )
		returned_value["time"].append( int( request.POST.get('time_' + str(i)) ) )

	return returned_value


def forms_pathcard(request):
	if request.method == "GET":
		try:
			choosen_station = Station.objects.get(id=request.GET.get('station'))
		except:
			projects = Project.objects.all()
			stations = Station.objects.all()
			context = {
				"projects": projects,
				"stations": stations,
				"warning_message": "Не выбрана станция",
			}
			return render(request, 'newpathcard.html', context)

		sets = WorkType.objects.filter(stationType=choosen_station.station).filter(custom=False)

		KKP_set = sets.filter(site='KKP')
		door_set = sets.filter(site='DUR')
		ventil_set = sets.filter(site='VNT')
		equip_set = sets.filter(site='EQI')
		electro_set = sets.filter(site='ELI')
		pipe_set = sets.filter(site='PIP')
		GRB_set = sets.filter(site='GRB')

		types = SiteType.objects.all()

		KKP_type = types.filter(site='KKP')
		door_type = types.filter(site='DUR')
		ventil_type = types.filter(site='VNT')
		equip_type = types.filter(site='EQI')
		electro_type = types.filter(site='ELI')
		pipe_type = types.filter(site='PIP')
		GRB_type = types.filter(site='GRB')

		overtype_KKP = fill_dict(KKP_set)
		overtype_equip = fill_dict(equip_set)
		overtype_electro = fill_dict(electro_set)
		overtype_pipe = fill_dict(pipe_set)
		overtype_GRB = fill_dict(GRB_set)

		context = {
			"station": request.GET.get('station'),
			
			"KKP_set": KKP_set,
			"door_set": door_set,
			"ventil_set": ventil_set,
			"equip_set": equip_set,
			"electro_set": electro_set,
			"pipe_set": pipe_set,
			"GRB_set": GRB_set,

			"KKP_type": KKP_type,
			"door_type": door_type,
			"ventil_type": ventil_type,
			"equip_type": equip_type,
			"electro_type": electro_type,
			"pipe_type": pipe_type,
			"GRB_type": GRB_type,

			"overtype_KKP": overtype_KKP,
			"overtype_equip": overtype_equip,
			"overtype_electro": overtype_electro,
			"overtype_pipe": overtype_pipe,
			"overtype_GRB": overtype_GRB,
		}
		return render(request, 'newpathcard2.html', context)
	
	if request.method == "POST":
		station_id = request.POST.get('station')
		station = Station.objects.get(id=station_id)

		station.left_to_card = False
		cur_pathcard = Pathcard.objects.create(station=station)

		posted_set = init_worktypes(request)
		
		wt_amount = int(request.POST.get('wt_amount'))
		for i in range(wt_amount):
			cur_work = WorkType.objects.get(id=posted_set["work_type"][i])
			cur_time = posted_set["time"][i]
			cur_qnt =  posted_set["quantity"][i]
			WorksOnPathcard.objects.create(work=cur_work,pathcard=cur_pathcard,time=cur_time, quantity=cur_qnt)
		
		context = {
			"success_message": "Маршрутная карта успешно добавлена",
		}

		station.save()
		return render(request, 'newpathcard2.html', context)


def get_time(request):
	site_type_id = request.GET.get('tool_id')
	cur_site_type = SiteType.objects.get(id=site_type_id)
	work_types = request.GET.getlist('work_types[]')

	return_data = []
	times = TimeForWork.objects.all()
	for item in work_types:
		cur_work = WorkType.objects.get(id=int(item))
		try:
			cur_time = times.get(work_type=cur_work, site_type=cur_site_type)
			return_data.append(cur_time.time)
		except:
			return_data.append(0)

	return JsonResponse({'data':return_data})


def get_description(request):
	wt_id = request.GET.get('item_id')
	worktype = WorkType.objects.get(id=wt_id)

	return_data = worktype.description
	return JsonResponse({'data':return_data})


def forms_order(request):
	if request.method == "GET":
		pathcard_id = request.GET.get('pathcard')
		works_on_pathcard = WorksOnPathcard.objects.filter(pathcard=pathcard_id)
		context = {
			"pathcard_id": pathcard_id,
			"works": works_on_pathcard,
		}

		return render(request, 'neworder.html', context)


def order_choose_pathcard(request):
	context = {
		"projects": Project.objects.all(),
	}
	return render(request, 'order/choose_pathcard.html', context)


def get_pathcards_for_order(request):
	project_id = request.GET.get('project_id')
	cur_project = Project.objects.get(id=project_id)
	stations = Station.objects.filter(project=cur_project)
	pathcards = []
	set_of_pc = Pathcard.objects.filter(station__in=stations)
	for item in set_of_pc:
		pathcard.append(item)
	amount = len(pathcards)
	print amount
	return JsonResponse({"pathcard":pathcards, "amount": amount})