# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-10-18 19:29
from __future__ import unicode_literals

from django.contrib.auth.management import create_permissions
from django.contrib.auth.hashers import make_password
from django.db import migrations
from guardian.conf import settings as guardian_settings
from guardian.shortcuts import assign_perm
from guardian.utils import get_anonymous_user
import metaci

def migrate_permissions(apps, schema_editor):
    for app_config in apps.get_app_configs():
        app_config.models_module = True
        create_permissions(app_config, apps=apps, verbosity=0)
        app_config.models_module = None

def create_groups_and_migrate_users(apps, schema_editor):
    Group = apps.get_model('auth.Group')
    Permission = apps.get_model('auth.Permission')
    User = apps.get_model('users.User')

    run_group = Group.objects.create(name='Run All Plans')
    run_group.permissions.add(
        Permission.objects.get(codename='run_plan')
    )

    view_group = Group.objects.create(name='View All Builds')
    view_group.permissions.add(
        Permission.objects.get(codename='view_builds')
    )

    rebuild_group = Group.objects.create(name='Rebuild All Builds')
    rebuild_group.permissions.add(
        Permission.objects.get(codename='rebuild_builds')
    )

    qa_group = Group.objects.create(name='QA All Builds')
    qa_group.permissions.add(
        Permission.objects.get(codename='qa_builds')
    )

    org_group = Group.objects.create(name='Login All Orgs')
    org_group.permissions.add(
        Permission.objects.get(codename='org_login')
    )


    users = User.objects.filter(is_staff = True, is_superuser = False)
    for user in users.iterator():
        user.groups.add(
            run_group,
            view_group,
            rebuild_group,
            qa_group,
            org_group,
        )
        # Since access is now granted through guardian, remove is_staff
        user.is_staff = False
        user.save()


def grant_anonymous_perms(apps, schema_editor):
    PlanRepository = apps.get_model('plan.PlanRepository')
    User = apps.get_model('users.User')
    try:
        anon = get_anonymous_user()
    except Exception as e:
        if not e.__class__.__name__ == 'DoesNotExist':
            raise
        anon = User(
            username=guardian_settings.ANONYMOUS_USER_NAME,
            password=make_password(None),
        )
        anon.save()
    for pr in PlanRepository.objects.all().iterator():
        if pr.plan.public is False:
            continue
        if pr.repo.public is False:
            continue
        assign_perm('plan.view_builds', anon, pr)
        

class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0021_auto_20181018_2143'),
    ]

    operations = [
        migrations.RunPython(migrate_permissions),
        migrations.RunPython(create_groups_and_migrate_users),
        migrations.RunPython(grant_anonymous_perms),
    ]

    complete_apps = ['auth','users']
