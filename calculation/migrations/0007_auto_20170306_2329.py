# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0006_auto_20170306_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='five',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='four',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='one',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='three',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='two',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, upload_to='calculation/'),
        ),
    ]
