# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-18 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0021_slot_split'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='split',
            field=models.NullBooleanField(default=None, help_text='Treat slot as Split Night (hdr propid must be in schedule lists)'),
        ),
    ]
