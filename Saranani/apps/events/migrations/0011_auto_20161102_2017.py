# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_auto_20161102_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='event_end',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='event_start',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
