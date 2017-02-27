# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0004_rezult'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rezult',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='csi',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='loyalty',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Rezult',
        ),
    ]
