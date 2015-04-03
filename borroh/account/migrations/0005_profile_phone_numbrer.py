# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20150403_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_numbrer',
            field=models.CharField(max_length=40, null=True, blank=True),
            preserve_default=True,
        ),
    ]
