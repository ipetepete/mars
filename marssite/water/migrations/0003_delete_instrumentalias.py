# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 16:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('water', '0002_auto_20170227_1155'),
    ]

    operations = [
        migrations.DeleteModel(
            name='InstrumentAlias',
        ),
    ]
