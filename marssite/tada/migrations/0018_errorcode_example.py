# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tada', '0017_auto_20170306_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='errorcode',
            name='example',
            field=models.TextField(blank=True, help_text='Example full error message.'),
        ),
    ]
