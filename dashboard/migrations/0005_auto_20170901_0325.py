# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 06:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_ticket_authodr'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='authodr',
            new_name='author',
        ),
    ]
