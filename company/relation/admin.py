# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from relation.models.basics import Employee, UserProfile, Gallery
# Register your models here.
admin.site.register(Employee)
admin.site.register(UserProfile)
admin.site.register(Gallery)

