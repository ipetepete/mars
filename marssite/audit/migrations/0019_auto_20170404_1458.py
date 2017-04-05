# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-04 21:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0018_auto_20170301_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditrecord',
            name='instrument',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tada.Instrument'),
        ),
        migrations.AlterField(
            model_name='auditrecord',
            name='telescope',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tada.Telescope'),
        ),
    ]
