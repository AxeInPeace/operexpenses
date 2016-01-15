# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect

def auth_registration(request):
	if request.method == "GET":
		return render(request, 'registration.html')
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('pass')
		confpass = request.POST.get('confpass')
		email = request.POST.get('email')

		if User.objects.filter(username=username):
			context = { "message": u"Имя уже существует", }
			return render(request, 'registration.html', context)
		
		if User.objects.filter(email=email):
			context = { "message": u"E-mail уже существует", }
			return render(request, 'registration.html', context)
		
		if password != confpass:
			context = { "message": u"Pass not match", }
			return render(request, 'registration.html', context)

		try:
			new_user = User.objects.create_user(username, email, password)
		except BaseException:
			context = {								
				"signup_error": "Registration error",
			}		
			return render(request, 'registration.html', context)
		#login(request, new_user)	
	return render(request, 'index.html')

@require_http_methods(["POST"])
def auth_login(request):
	username = request.POST.get('username')
	password = request.POST.get('pass')
	user = authenticate(username=username, password=password)
	if user is None:
		context = {						
			"signin_error": "User not found, probably you write wrong password or login",
		}	
		return render(request, 'index.html', context)
	else:
		login(request, user)
		return render(request, 'index.html')

def auth_logout(request):
	logout(request)	
	return HttpResponseRedirect("/")
