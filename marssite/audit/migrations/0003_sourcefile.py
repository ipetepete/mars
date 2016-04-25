# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0002_auto_20151130_0753'),
    ]

    operations = [
        migrations.CreateModel(
            name='SourceFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(help_text='Path of file as submitted', max_length=256)),
                ('when', models.DateTimeField(auto_now_add=True, help_text='When recorded')),
            ],
            options={
                'ordering': ('when',),
            },
        ),
    ]