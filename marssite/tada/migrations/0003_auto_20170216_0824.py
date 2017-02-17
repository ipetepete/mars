# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tada', '0002_fileprefix'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('code', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='ProcType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('code', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='ProdType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('code', models.CharField(max_length=1)),
            ],
        ),
        migrations.RenameModel(
            old_name='TacIntrument',
            new_name='TacInstrument',
        ),
    ]