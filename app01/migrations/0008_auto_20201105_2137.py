# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-11-05 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_auto_20201105_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='project_jindu',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
