# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-18 21:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0005_remove_changebalance_period'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='changebalance',
            options={'ordering': ('-id', 'sum'), 'verbose_name': 'Изменение', 'verbose_name_plural': 'Изменения'},
        ),
        migrations.AddField(
            model_name='changebalance',
            name='date',
            field=models.DateField(null=True, verbose_name='Дата:'),
        ),
    ]
