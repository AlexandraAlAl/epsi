# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='extuser',
            name='day_licenz',
            field=models.IntegerField(verbose_name='Дней до конца лицензии', default=0),
        ),
        migrations.AddField(
            model_name='extuser',
            name='myURL',
            field=models.CharField(verbose_name='URL', max_length=10, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='extuser',
            name='name_comp',
            field=models.CharField(verbose_name='Наименование компании', max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='extuser',
            name='phone',
            field=models.CharField(verbose_name='Телефон', max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='extuser',
            name='is_admin',
            field=models.BooleanField(verbose_name='Вход в админку', default=False),
        ),
    ]
