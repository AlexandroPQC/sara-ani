# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 20:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0016_remove_placeschedule_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='event_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='event_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]