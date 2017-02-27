# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculation', '0003_auto_20170216_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rezult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('csi', models.IntegerField()),
                ('loyalty', models.IntegerField()),
                ('post', models.ForeignKey(to='calculation.Post')),
            ],
        ),
    ]
