# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0005_auto_20170225_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file_name',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, upload_to='calculation'),
        ),
    ]
