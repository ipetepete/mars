# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 02:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0017_auto_20170227_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditrecord',
            name='instrument',
            field=models.CharField(choices=[('arcoiris', 'arcoiris'), ('whirc', 'whirc'), ('decam', 'decam'), ('90prime', '90prime'), ('goodman', 'goodman'), ('spartan', 'spartan'), ('echelle', 'echelle'), ('flamingos', 'flamingos'), ('ice', 'ice'), ('chiron', 'chiron'), ('cosmos', 'cosmos'), ('newfirm', 'newfirm'), ('y4kcam', 'y4kcam'), ('falmingos', 'falmingos'), ('wildfire', 'wildfire'), ('mosaic', 'mosaic'), ('osiris', 'osiris'), ('soi', 'soi'), ('sami', 'sami'), ('ispi', 'ispi'), ('gtcam', 'gtcam'), ('ccd_imager', 'ccd_imager'), ('goodman spectrograph', 'goodman spectrograph'), ('bench', 'bench'), ('andicam', 'andicam'), ('(p)odi', '(p)odi'), ('kosmos', 'kosmos'), ('spartan ir camera', 'spartan ir camera'), ('arcon', 'arcon'), ('hdi', 'hdi'), ('mop/ice', 'mop/ice'), ('minimo/ice', 'minimo/ice'), ('mosaic3', 'mosaic3')], max_length=25),
        ),
    ]
