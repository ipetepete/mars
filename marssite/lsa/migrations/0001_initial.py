# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-29 23:07
from __future__ import unicode_literals

from django.db import connections
from django.db import migrations


def read_sql(apps, schema_editor):
    cursor = connections['archive'].cursor()

    # This should be done by provisioning (as posgres superuser)
    #!with open('globals-dump.sql') as f:
    #!    sql = f.read()
    #!cursor.execute(sql)
    with open('/etc/mars/lsa-schema.metadata.sql') as f:
        sql = f.read()
    cursor.execute(sql)
    #!print('DBG: apply sql:',sql)
    return None

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        #! migrations.RunPython(read_sql)
    ]

    
