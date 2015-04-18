# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20150410_1435'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(blank=True, to='cart.Cart', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, max_length=40, null=True, choices=[(b'pending', b'pending'), (b'done', b'done'), (b'cancel', b'cancel')]),
            preserve_default=True,
        ),
    ]
