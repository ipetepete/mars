# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-23 18:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('natica', '0002_auto_20170502_1328'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('filesize', models.BigIntegerField()),
                ('release_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Hdu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hdu_index', models.IntegerField()),
                ('object', models.CharField(max_length=80)),
                ('survey', models.CharField(max_length=80)),
                ('survey_id', models.CharField(max_length=80)),
                ('prop_id', models.CharField(max_length=80)),
                ('start_date', models.DateTimeField()),
                ('ra', models.FloatField()),
                ('dec', models.FloatField()),
                ('equinox', models.FloatField()),
                ('naxes', models.IntegerField()),
                ('naxis_length', models.CharField(max_length=80)),
                ('mimetype', models.CharField(max_length=80)),
                ('instrument', models.CharField(max_length=80)),
                ('telescope', models.CharField(max_length=80)),
                ('pixflags', models.CharField(max_length=80)),
                ('bandpass_id', models.CharField(max_length=80)),
                ('bandpass_unit', models.CharField(max_length=80)),
                ('bandpass_lolimit', models.CharField(max_length=80)),
                ('bandpass_hilimit', models.CharField(max_length=80)),
                ('exposure', models.FloatField()),
                ('depth', models.FloatField()),
                ('depth_err', models.CharField(max_length=80)),
                ('magzero', models.FloatField()),
                ('magerr', models.FloatField()),
                ('seeing', models.FloatField()),
                ('airmass', models.FloatField()),
                ('astrmcat', models.CharField(max_length=80)),
                ('biasfil', models.CharField(max_length=80)),
                ('bunit', models.CharField(max_length=80)),
                ('dqmask', models.CharField(max_length=80)),
                ('darkfil', models.CharField(max_length=80)),
                ('date_obs', models.DateTimeField()),
                ('flatfil', models.CharField(max_length=80)),
                ('ds_ident', models.CharField(max_length=80)),
                ('efftime', models.FloatField()),
                ('filter', models.CharField(max_length=80)),
                ('filtid', models.CharField(max_length=80)),
                ('frngfil', models.CharField(max_length=80)),
                ('ha', models.FloatField()),
                ('instrume', models.CharField(max_length=80)),
                ('md5sum', models.CharField(max_length=80)),
                ('mjd_obs', models.FloatField()),
                ('obs_elev', models.FloatField()),
                ('obs_lat', models.FloatField()),
                ('obs_long', models.FloatField()),
                ('photbw', models.FloatField()),
                ('photclam', models.FloatField()),
                ('photfwhm', models.FloatField()),
                ('pipeline', models.CharField(max_length=80)),
                ('plver', models.CharField(max_length=80)),
                ('proctype', models.CharField(max_length=80)),
                ('prodtype', models.CharField(max_length=80)),
                ('puplfil', models.CharField(max_length=80)),
                ('radesys', models.CharField(max_length=80)),
                ('rawfile', models.CharField(max_length=80)),
                ('sb_recno', models.IntegerField()),
                ('sflatfil', models.CharField(max_length=80)),
                ('timesys', models.CharField(max_length=80)),
                ('disper', models.CharField(max_length=80)),
                ('obsmode', models.CharField(max_length=80)),
                ('filename', models.CharField(max_length=80)),
                ('nocslit', models.CharField(max_length=80)),
                ('nocssn', models.CharField(max_length=80)),
                ('zd', models.FloatField()),
                ('rspgrp', models.CharField(max_length=80)),
                ('rsptgrp', models.CharField(max_length=80)),
                ('reject', models.CharField(max_length=80)),
                ('seqid', models.CharField(max_length=80)),
                ('plqname', models.CharField(max_length=80)),
                ('pldname', models.CharField(max_length=80)),
                ('fk5coords', models.CharField(max_length=80)),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='natica.File')),
                ('primary_hdu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='natica.Hdu')),
            ],
        ),
    ]
