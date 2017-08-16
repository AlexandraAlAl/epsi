# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0008_auto_20170717_0350'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='delete_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 16, 20, 40, 58, 317226, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='csi',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='five',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='four',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='loyalty',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='one',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='regress',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='three',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='two',
            field=models.FloatField(default=0),
        ),
    ]
