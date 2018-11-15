# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-11-15 01:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Typeinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='品牌名')),
                ('logo', models.ImageField(upload_to='static/images/logo', verbose_name='logo')),
                ('isDelete', models.BooleanField(default=False, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '品牌表',
                'verbose_name_plural': '品牌表',
                'db_table': 'Type',
            },
        ),
    ]
