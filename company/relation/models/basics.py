# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# def get_image_path(instance, filename):
#     return os.path.join('photos', str(instance.id), filename)


class Employee(models.Model):
    DOCUBE, JIFFY = range(1, 3)
    ENGINEERING, QA, IMPLEMENTATION, ADMINISTRATION = range(1, 5)
    TEAM = ((DOCUBE, 'DOCUBE'), (JIFFY, 'JIFFY'))
    SUB_TEAM = ((ENGINEERING, 'ENGINEERING'), (QA, 'QA'), (IMPLEMENTATION, 'IMPLEMENTATION'), (ADMINISTRATION, 'ADMINISTRATION'))
    name = models.CharField(max_length=100)
    team = models.PositiveIntegerField(choices=TEAM, default=JIFFY)
    sub_team = models.PositiveIntegerField(choices=SUB_TEAM, default=ENGINEERING)
    designation = models.CharField(max_length=100,  null=True, blank=True)
    phone_number = models.CharField(max_length=100,  null=True, blank=True)
    email = models.CharField(max_length=100,  null=True, blank=True)
    employee_id = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    blood_group = models.CharField(max_length=100, default='Blood group information is not available')
    date_of_birth = models.CharField(max_length=100, default='DOB is not available')
    brief_description = models.CharField(max_length=2000, default='Description is not available')
    emergency_contact_number = models.CharField(max_length=100, default='Emergency contact number is not available')
    date_of_join = models.CharField(max_length=100, default='This information is not available')
    image = models.ImageField(upload_to='team_members/', default='team_members/None/no-img.jpg')

    class Meta:
        app_label = 'relation'

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)







# class EciUser(models.Model):
#     username = models.CharField(max_length=100)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)

#     class Meta:
#         app_label = 'relation'

#     def verify_password(self,password):
#         orig_passwd = self.password
#         if password == orig_passwd:
#             return True
#         else:
#             return False