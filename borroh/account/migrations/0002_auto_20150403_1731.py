# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='account',
            name='user',
        ),
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]