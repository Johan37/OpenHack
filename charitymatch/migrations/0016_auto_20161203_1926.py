# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-03 19:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charitymatch', '0015_auto_20161203_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='methods',
            field=models.ManyToManyField(to='charitymatch.Method'),
        ),
    ]
