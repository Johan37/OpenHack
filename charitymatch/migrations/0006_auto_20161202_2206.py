# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charitymatch', '0005_auto_20161202_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='charitymatch/static/charitymatch/organisations/image'),
        ),
    ]
