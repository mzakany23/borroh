# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_cart_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='active',
        ),
        migrations.AddField(
            model_name='cart',
            name='contains_borroh_order',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cart',
            name='contains_buy_order',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
