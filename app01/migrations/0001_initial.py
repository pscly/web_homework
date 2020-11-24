# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-11-24 01:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('img_path', models.FileField(upload_to='img/Com')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Fen_lei',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fen_lei_name', models.CharField(max_length=255)),
                ('count_click_1', models.IntegerField()),
                ('bei_zhu', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=255)),
                ('file_path_name', models.CharField(max_length=255)),
                ('file_path', models.FileField(upload_to='user_file/%Y_%m/')),
                ('file_date', models.DateTimeField(auto_now_add=True)),
                ('is_look', models.BooleanField(default=1)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('count_click', models.IntegerField(default=0)),
                ('is_ban', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
                ('is_root', models.BooleanField(default=0)),
                ('is_vip', models.BooleanField(default=0)),
                ('money', models.DecimalField(decimal_places=2, max_digits=12)),
                ('user_ico', models.FileField(default='user_ico/01default.jpg', upload_to='user_ico/%Y/')),
                ('is_ban', models.BooleanField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='files',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.User'),
        ),
    ]
