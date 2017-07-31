# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from relation.models import Employee
from relation.models import EciUser

# Register your models here.
admin.site.register(Employee)
admin.site.register(EciUser)
