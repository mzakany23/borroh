# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_order_date_order_started'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='borroh_order',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='buy_order',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
