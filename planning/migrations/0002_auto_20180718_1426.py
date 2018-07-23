# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-18 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeBalance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, verbose_name='Наименование')),
                ('category', models.CharField(choices=[('Income', 'Зарплата'), ('Spending', 'Растрата')], max_length=20, verbose_name='Категория')),
            ],
        ),
        migrations.AddField(
            model_name='period',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание периода'),
        ),
        migrations.AlterField(
            model_name='period',
            name='end_day',
            field=models.DateField(verbose_name='Конец периода'),
        ),
        migrations.AlterField(
            model_name='period',
            name='name',
            field=models.CharField(blank=True, max_length=30, verbose_name='Название периода'),
        ),
        migrations.AlterField(
            model_name='period',
            name='start_day',
            field=models.DateField(verbose_name='Начало периода'),
        ),
    ]