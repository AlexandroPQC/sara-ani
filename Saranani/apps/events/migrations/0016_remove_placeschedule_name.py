# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 20:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_placeschedule_schedules'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='placeschedule',
            name='name',
        ),
    ]