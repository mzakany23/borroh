# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20150418_1828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='borroh_order',
        ),
        migrations.RemoveField(
            model_name='order',
            name='buy_order',
        ),
        migrations.AddField(
            model_name='order',
            name='type_of_cart',
            field=models.CharField(blank=True, max_length=40, null=True, choices=[(b'Buy', b'Buy'), (b'Borroh', b'Borroh')]),
            preserve_default=True,
        ),
    ]
