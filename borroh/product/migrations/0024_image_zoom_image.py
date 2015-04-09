# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0023_auto_20150407_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='zoom_image',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
