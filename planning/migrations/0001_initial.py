# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-18 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, verbose_name='Название периода: ')),
                ('start_day', models.DateField(auto_now=True, verbose_name='Начало периода: ')),
                ('end_day', models.DateField(auto_now=True, verbose_name='Конец периода: ')),
            ],
            options={
                'verbose_name': 'Период',
                'verbose_name_plural': 'Периоды',
            },
        ),
    ]
