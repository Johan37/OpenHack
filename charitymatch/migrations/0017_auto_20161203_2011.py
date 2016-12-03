# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-03 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charitymatch', '0016_auto_20161203_1926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organisation',
            name='countries',
        ),
        migrations.AddField(
            model_name='organisation',
            name='regions',
            field=models.ManyToManyField(to='charitymatch.Region'),
        ),
    ]