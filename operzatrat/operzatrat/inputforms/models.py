# -*- coding: utf-8 -*-
from django.db import models


class Project(models.Model):
	def __unicode__(self):
		return self.name

	start_date = models.DateField(default=None, blank=True, null=True)
	end_date = models.DateField(default=None, blank=True, null=True)
	name = models.CharField(max_length = 255)


class StationType(models.Model):
	def __unicode__(self):
		return self.name

	name = models.CharField(max_length = 255,unique=True)


class Station(models.Model):
	def __unicode__(self):
		return self.station.name + ' on ' + self.project.name

	station = models.ForeignKey(StationType)
	project = models.ForeignKey(Project)
	left_to_card = models.BooleanField(default=True)


SITES = (
	('BLK', u'Блок'),
	('CNT', u'Контейнер'),
	('SKD', u'СКИД'),
	('KKP', u'Сборка станции'),
	('DUR', u'Сборка двери'),
	('VNT', u'Вентиляционная решётка'),
	('EQI', u'Монтаж ОТ оборудования'),
	('ELI', u'Монтаж электрооборудования'),
	('PIP', u'KVF-трубопровод'),
	('GRB', u'ГРБ'),
)

class WorkOvertype(models.Model):
	def __unicode__(self):
		return self.name

	name = models.CharField(max_length=1023)
	#custom = models.BooleanField(default=False)

class WorkType(models.Model):
	def __unicode__(self):
		return self.name

	name = models.CharField(max_length=1023)
	description = models.TextField(blank=True, null=True)
	stationType = models.ManyToManyField(StationType)
	site = models.CharField(max_length=3, choices=SITES, blank=True, null=True)
	owned_to = models.ForeignKey(WorkOvertype, blank=True, null=True, default=-1)
	custom = models.BooleanField(default=False)


class SiteType(models.Model):
	def __unicode__(self):
		return self.name + ' on ' + self.site

	name = models.CharField(max_length=1023)
	site = models.CharField(max_length=3, choices=SITES)


class TimeForWork(models.Model):
	def __unicode__(self):
		return self.work_type.name + ' ' + self.site_type.name

	work_type = models.ForeignKey(WorkType)
	site_type = models.ForeignKey(SiteType)
	time = models.IntegerField()


class Pathcard(models.Model):
	def __unicode__(self):
		return self.station.__unicode__()

	#station = models.OneToOne(Station)
	station = models.ForeignKey(Station)
	#closed = models.BooleanField(default=False)


class WorksOnPathcard(models.Model):
	def __unicode__(self):
		return self.work.name + ' on ' 	+ self.pathcard.__unicode__() + ' with time ' + str(self.time)

	work = models.ForeignKey(WorkType)
	pathcard = models.ForeignKey(Pathcard)
	time = models.IntegerField()
	quantity = models.IntegerField()


"""
class Worker(models.Model):
	def __unicode__(self):
		return self.name

	name = models.CharField(max_length=2013)
	occupation = models.ForeignKey(Occupation)


class Order(models.Model):
	def __unicode__(self):
		return self.work

	worker = models.ForeignKey(Worker)
	work = models.ForeignKey(WorksOnPathcard)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	fact_end_time = models.DateTimeField(default=None, blank=True, null=True)
"""