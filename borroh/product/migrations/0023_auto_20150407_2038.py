# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0022_auto_20150407_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='points_price',
            field=models.IntegerField(default=0, max_length=40, null=True, blank=True),
            preserve_default=True,
        ),
    ]
