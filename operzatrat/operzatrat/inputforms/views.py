# -*- coding: utf-8 -*-
#TODO: Добавить модель объектов
#TODO: Расширить на объекты
#TODO: Заполнить БД
#TODO: Сабмит при корректной форме
#TODO: Сейв не зависит от корректности формы
#TODO:

from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect, JsonResponse


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

        if project_name == "a":
            context["warning_message"] = u"Пожалуйста, введите имя проекта"
            return render(request, 'newproject.html', context)

        fields_num = request.POST.get('fields_num')
        if fields_num == "" or fields_num == "0":
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

        if start_date == "" or end_date == "":
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


def init_worktypes(request, custom_wot):
    wt_amount = int(request.POST.get('wt_amount'))
    custom_wt_amount = int(request.POST.get('custom_wt_amount'))
    returned_value = {
        "work_type": [],
        "quantity": [],
        "time": [],
    }
    for i in range(wt_amount):
        returned_value["work_type"].append(int(request.POST.get('wt_' + str(i))))
        returned_value["quantity"].append(int(request.POST.get('qnt_' + str(i))))
        returned_value["time"].append(float(request.POST.get('time_' + str(i))))
    custom_wt = []
    for i in range(wt_amount, wt_amount + custom_wt_amount):
        owner_str = request.POST.get('owner_' + str(i))
        cur_site = request.POST.get('site_' + str(i))
        if owner_str == "None":
            curwt = WorkType.objects.create(name=request.POST.get('wt_' + str(i)), custom=True, owned_to_id=-1, site=cur_site)
        else:
            owner_id = int(owner_str)
            # negative and 0 means that owner is custom overtype
            if owner_id <= 0:
                owner = custom_wot[-owner_id]
            else:
                owner = WorkOvertype.objects.get(id=owner_id)
            curwt = WorkType.objects.create(name=request.POST.get('wt_' + str(i)), custom=True, owned_to=owner, site=cur_site)
        custom_wt.append(curwt)
        returned_value["work_type"].append(curwt.id)
        returned_value["quantity"].append(int(request.POST.get('qnt_' + str(i))))
        returned_value["time"].append(float(request.POST.get('time_' + str(i))))
    return returned_value


def generate_pathcard_context(choosen_station):
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
    overtype_door = fill_dict(door_set)
    overtype_ventil = fill_dict(ventil_set)
    overtype_equip = fill_dict(equip_set)
    overtype_electro = fill_dict(electro_set)
    overtype_pipe = fill_dict(pipe_set)
    overtype_GRB = fill_dict(GRB_set)

    context = {
        "station": choosen_station.id,

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
        "overtype_door": overtype_door,
        "overtype_ventil": overtype_ventil,
        "overtype_equip": overtype_equip,
        "overtype_electro": overtype_electro,
        "overtype_pipe": overtype_pipe,
        "overtype_GRB": overtype_GRB,
    }
    return context


def forms_pathcard(request):
    if request.method == "GET":
        try:
            choosen_station = Station.objects.get(id=request.GET.get('station'))
        except: #station not choosen
            stations = Station.objects.filter(left_to_card=True)
            projects = []
            for station in stations:
                if station.project not in projects:
                    projects.append(station.project)
            context = {
                "projects": projects,
                "stations": stations,
                "warning_message": "Не выбрана станция",
            }
            return render(request, 'newpathcard.html', context)
        try: #load pathcard
            cur_pathcard = Pathcard.objects.get(station=choosen_station)
            works = WorksOnPathcard.objects.filter(pathcard=cur_pathcard)
            context = generate_pathcard_context(choosen_station)
            choosen_works = {}
            custom_overtypes = {}
            for item in SITES:
                custom_overtypes[item[0]] = []

            for work in works:
                if work.work.owned_to not in choosen_works:
                    choosen_works[work.work.owned_to] = []
                    if work.work.owned_to != None and work.work.owned_to.custom:
                        custom_overtypes[work.work.site].append(work.work.owned_to)
                choosen_works[work.work.owned_to].append(work)
            context['choosen_works'] = choosen_works
            context['custom_overtypes'] = custom_overtypes
            context['cur_pathcard'] = cur_pathcard
            return render(request, 'pathcard_template.html', context)
        except: #new pathcard
            context = generate_pathcard_context(choosen_station)
            return render(request, 'pathcard_template.html', context)

    if request.method == "POST":
        try:
            station_id = request.POST.get('station')
            station = Station.objects.get(id=station_id)
        except:
            context = {
                "warning_message": "Станция не найдена",
            }
            return render(request, 'index.html', context)

        try:
            cur_pathcard = Pathcard.objects.get(station=station)
            old_works_on_pathcards = WorksOnPathcard.objects.filter(pathcard=cur_pathcard)
            old_works = []
            old_custom_wt = []
            old_overtypes = []

            for w in old_works_on_pathcards:
                old_works.append(w.work)
                if w.work.custom:
                    old_custom_wt.append(w.work)
                    if (w.work.owned_to not in old_overtypes) and w.work.owned_to.custom:
                        old_overtypes.append(w.work.owned_to)
            flag_overrecord = True
        except:
            flag_overrecord = False

        try:
            overtypes = init_overtypes(request)
        except:
            context = {
                "warning_message": "Операции не были созданы",
            }
            return render(request, 'index.html', context)

        try:
            posted_set = init_worktypes(request, overtypes)
        except:
            delete_overtypes(overtypes)
            context = {
                "warning_message": "Работы не были проинициализированны",
            }
            return render(request, 'index.html', context)

        try:
            cur_pathcard, is_created = Pathcard.objects.get_or_create(station=station)
            cur_pathcard.kkp_site_type = SiteType.objects.get(id=int(request.POST.get('KKP_type')))
            cur_pathcard.door_site_type = SiteType.objects.get(id=int(request.POST.get('door_type')))
            cur_pathcard.ventil_site_type = SiteType.objects.get(id=int(request.POST.get('ventil_type')))
            cur_pathcard.eqi_site_type = SiteType.objects.get(id=int(request.POST.get('equip_type')))
            cur_pathcard.eli_site_type = SiteType.objects.get(id=int(request.POST.get('electro_type')))
            cur_pathcard.pipe_site_type = SiteType.objects.get(id=int(request.POST.get('pipe_type')))
            cur_pathcard.grb_site_type = SiteType.objects.get(id=int(request.POST.get('GRB_type')))
            cur_pathcard.save()
        except:
            delete_overtypes(overtypes)
            context = {
                "warning_message": "Машрутная карта не найдена или не может быть создана",
            }
            return render(request, 'index.html', context)
        wt_amount = int(request.POST.get('wt_amount'))
        custom_wt_amount = int(request.POST.get('custom_wt_amount'))
        for i in range(wt_amount + custom_wt_amount):
            cur_work = WorkType.objects.get(id=posted_set["work_type"][i])
            cur_time = posted_set["time"][i]
            cur_qnt = posted_set["quantity"][i]
            WorksOnPathcard.objects.create(work=cur_work, pathcard=cur_pathcard, time=cur_time, quantity=cur_qnt)
            if cur_work.site == "DUR" or cur_work.site == "VNT":
                pass
        if request.POST.get('save_flag') == "True":
            station.left_to_card = True
        elif request.POST.get('save_flag') == "False":
            station.left_to_card = False
        station.save()
        context = {
            "success_message": "Маршрутная карта успешно добавлена",
        }
        if flag_overrecord:
            for item in old_works_on_pathcards:
                item.delete()
            for item in old_custom_wt:
                item.delete()
            for item in old_overtypes:
                item.delete()

        return render(request, 'index.html', context)


def get_time(request):
    site_type_id = request.GET.get('tool_id')
    cur_site_type = SiteType.objects.get(id=int(site_type_id))
    work_type = request.GET.get('work_id')
    try:
        time_for_work = TimeForWork.objects.get(work_type_id=int(work_type), site_type=cur_site_type)
        time = time_for_work.time
    except:
        time = 0
    return JsonResponse({'time': time})


def get_description(request):
    wt_id = request.GET.get('item_id')
    try:
        worktype = WorkType.objects.get(id=wt_id)
        return_data = worktype.description
    except:
        return_data = "Описание не найдено."
    return JsonResponse({'data': return_data})


def init_overtypes(request):
    amount = int(request.POST.get('custom_wot_amount'))
    overtypes = []
    for i in range(amount):
        name = request.POST.get('custom_ot_' + str(i))
        if name == None:
            name = ""
        site = request.POST.get('overtype_site_' + str(i))
        overtype = WorkOvertype.objects.create(name=name, custom=True, site=site)
        overtypes.append(overtype)
    return overtypes


def delete_overtypes(overtypes):
    for item in overtypes:
        item.delete()


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
        pathcards.append(item)
    amount = len(pathcards)
    return JsonResponse({"pathcard": pathcards, "amount": amount})


def edit_start(request):
    return render(request, 'startedit.html')


def edit_choose_pathcard(request):
    not_closed_stations = Station.objects.filter(left_to_card=True)
    pathcards = Pathcard.objects.filter(station__in=not_closed_stations)
    context = {
        'pathcards': pathcards,
    }
    return render(request, 'edit_choose_pathcard.html', context)


def edit_pathcard(request):
    if request.method == "GET":
        return render(request, 'pathcard_template.html')