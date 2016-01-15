# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *

# Register your models here.
admin.site.register(Project)
admin.site.register(Station)
admin.site.register(StationType)
admin.site.register(WorkType)
admin.site.register(WorkOvertype)
admin.site.register(SiteType)
admin.site.register(TimeForWork)
admin.site.register(Pathcard)
admin.site.register(WorksOnPathcard)
