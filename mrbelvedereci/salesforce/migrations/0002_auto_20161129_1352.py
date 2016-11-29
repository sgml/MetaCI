# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 13:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0002_repository_github_id'),
        ('salesforce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Org',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('json', models.TextField()),
                ('scratch', models.BooleanField(default=False)),
                ('repo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orgs', to='github.Repository')),
            ],
        ),
        migrations.DeleteModel(
            name='OrgConfig',
        ),
    ]