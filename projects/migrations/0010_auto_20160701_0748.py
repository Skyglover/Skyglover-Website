# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-01 07:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20160701_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2016, 7, 1, 7, 48, 49, 764369)),
        ),
    ]
