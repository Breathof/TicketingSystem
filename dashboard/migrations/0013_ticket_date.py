# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-07 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_auto_20170907_0232'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]