# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-06 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0003_auto_20161213_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]