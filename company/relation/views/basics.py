# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
# Create your views here.

    
@login_required
def get_homepage(request, *args, **kwargs):
	return render(request, 'index.html')

class OutingPageView(TemplateView):
    def get(request, **kwargs):
        return render(request, 'charts.html', context=None)

class TeamListView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'team_list.html', context=None)


def user_login(request,*args, **kwargs):
	if request.method == "POST":
		# import pdb; pdb.set_trace()
		username = request.POST.get('u',None)
		password = request.POST.get('p',None)
		user = authenticate(username=username, password=password)
		if user is not None:
		    # A backend authenticated the credentials
		    login(request, user)
		    return render(request, 'index.html',{'user': user})
		else:
		    # No backend authenticated the credentials
			return render(request, 'login.html')
	if request.method == "GET":
		return render(request,'login.html')

def user_logout(request):
    logout(request)
    return render(request,'login.html')

def get_userprofile(request):
	return render(request, 'profile.html')