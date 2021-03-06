# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-26 12:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basescore',
            name='area',
        ),
        migrations.RemoveField(
            model_name='basescore',
            name='depth',
        ),
        migrations.RemoveField(
            model_name='basescore',
            name='fetch',
        ),
        migrations.RemoveField(
            model_name='basescore',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='basescore',
            name='lon',
        ),
        migrations.RemoveField(
            model_name='basescore',
            name='tide_range',
        ),
        migrations.RemoveField(
            model_name='basescore',
            name='trib_count',
        ),
        migrations.RemoveField(
            model_name='basescore',
            name='trib_width',
        ),
        migrations.RemoveField(
            model_name='basescore',
            name='turbidity',
        ),
        migrations.RemoveField(
            model_name='basescore',
            name='ufarea',
        ),
        migrations.RemoveField(
            model_name='basescore',
            name='velocity',
        ),
        migrations.RemoveField(
            model_name='basescore',
            name='waveheight',
        ),
        migrations.RemoveField(
            model_name='basescore',
            name='wind_velocity',
        ),
    ]
