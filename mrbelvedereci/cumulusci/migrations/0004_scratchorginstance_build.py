# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-02 17:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0003_auto_20170201_1518'),
        ('cumulusci', '0003_auto_20170202_0807'),
    ]

    operations = [
        migrations.AddField(
            model_name='scratchorginstance',
            name='build',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scratch_orgs', to='build.Build'),
        ),
    ]
