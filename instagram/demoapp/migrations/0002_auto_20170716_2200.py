# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 16:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='phone',
            new_name='mobile',
        ),
    ]
