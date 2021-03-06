# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-15 13:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20161026_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Data Source')),
                ('base_url', models.URLField(blank=True, max_length=255, verbose_name='Base Url')),
                ('query_string', models.CharField(blank=True, max_length=255, verbose_name='Query String')),
                ('access_token', models.CharField(blank=True, max_length=255, verbose_name='Access Token')),
                ('response_format', models.CharField(blank=True, max_length=30, verbose_name='Response Format')),
                ('request_url', models.URLField(blank=True, max_length=500, verbose_name='Request URL')),
                ('reference_url', models.URLField(blank=True)),
            ],
        ),
    ]
