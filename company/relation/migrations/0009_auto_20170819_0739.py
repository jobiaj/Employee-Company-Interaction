# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-19 07:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relation', '0008_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='tags',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='uploaded_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
