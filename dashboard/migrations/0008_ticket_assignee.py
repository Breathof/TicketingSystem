# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_remove_ticket_assignee'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='assignee',
            field=models.CharField(default='Jaime', max_length=100),
            preserve_default=False,
        ),
    ]