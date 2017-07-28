# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class OutingPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'charts.html', context=None)

class TeamListView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'team_list.html', context=None)