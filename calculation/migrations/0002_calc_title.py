# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calc',
            name='title',
            field=models.CharField(max_length=200, default='aaaa'),
            preserve_default=False,
        ),
    ]
