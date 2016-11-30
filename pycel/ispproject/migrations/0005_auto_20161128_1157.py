# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-28 11:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ispproject', '0004_auto_20161128_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_visible',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='change_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 28, 11, 57, 12, 252967, tzinfo=utc), verbose_name=b'change date'),
        ),
    ]
