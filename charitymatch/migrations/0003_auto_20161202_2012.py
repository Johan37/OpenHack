# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 20:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charitymatch', '0002_auto_20161122_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='description',
            field=models.CharField(default='blank', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organisation',
            name='link',
            field=models.CharField(default='www.internet.com', max_length=200),
            preserve_default=False,
        ),
    ]
