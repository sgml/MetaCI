# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-02 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cumulusci', '0004_scratchorginstance_build'),
    ]

    operations = [
        migrations.AddField(
            model_name='scratchorginstance',
            name='delete_error',
            field=models.TextField(blank=True, null=True),
        ),
    ]
