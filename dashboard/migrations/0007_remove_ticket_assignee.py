# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 06:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_remove_ticket_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='assignee',
        ),
    ]
