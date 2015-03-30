# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20150330_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='points_price',
            field=models.IntegerField(default=0, max_length=40),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(default=0.0, max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, max_length=40, null=True, choices=[(b'XS', b'XS'), (b'S', b'M'), (b'L', b'L'), (b'XS', b'XL'), (b'XXL', b'XXL')]),
            preserve_default=True,
        ),
    ]
