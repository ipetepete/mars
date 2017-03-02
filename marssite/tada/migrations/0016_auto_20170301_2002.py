# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 03:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tada', '0015_auto_20170301_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='TacInstrumentAlias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tac', models.CharField(help_text='Name used by Dave Bells TAC Schedule', max_length=20, unique=True)),
                ('hdr', models.CharField(help_text='Name used in FITS header', max_length=20, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='TacInstrum',
        ),
        migrations.DeleteModel(
            name='TacInstrument',
        ),
    ]
