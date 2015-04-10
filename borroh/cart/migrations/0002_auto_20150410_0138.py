# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='items',
        ),
        migrations.AddField(
            model_name='lineitem',
            name='cart',
            field=models.ForeignKey(blank=True, to='cart.Cart', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lineitem',
            name='product',
            field=models.ForeignKey(blank=True, to='product.Product', null=True),
            preserve_default=True,
        ),
    ]
