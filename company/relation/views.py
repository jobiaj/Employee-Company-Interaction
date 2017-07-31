# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from relation.models import EciUser
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
		username = request.POST.get('u',None)
		password = request.POST.get('p',None)
		crrnt_user = EciUser.objects.get(username=username)
		if crrnt_user.verify_password(password):
			return render(request, 'index.html')
		else:
			return render(request, 'login_dummy.html')
	if request.method == "GET":
		return render(request,'login_dummy.html')