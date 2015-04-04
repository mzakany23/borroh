# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20150404_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='default',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
