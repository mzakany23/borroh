# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_remove_order_shipping'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='free_shipping',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
