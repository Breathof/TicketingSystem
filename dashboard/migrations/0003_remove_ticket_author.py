# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 06:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20170901_0050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='author',
        ),
    ]