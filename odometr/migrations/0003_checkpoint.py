# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 14:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('odometr', '0002_auto_20160602_1421'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkpoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mileage', models.PositiveIntegerField()),
                ('log_date', models.DateTimeField(verbose_name='date of mileage')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='odometr.Car')),
            ],
        ),
    ]
