# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-09 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0003_auto_20171009_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicledetails',
            name='registration_no',
            field=models.CharField(max_length=15),
        ),
    ]
