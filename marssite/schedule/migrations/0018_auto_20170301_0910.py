# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0017_auto_20160615_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='instrument',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='slot',
            name='telescope',
            field=models.CharField(max_length=10),
        ),
    ]
