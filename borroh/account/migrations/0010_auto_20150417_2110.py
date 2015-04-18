# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_profile_subscription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='phone_numbrer',
            new_name='name',
        ),
        migrations.AddField(
            model_name='address',
            name='phone_number',
            field=models.CharField(max_length=40, null=True, blank=True),
            preserve_default=True,
        ),
    ]
