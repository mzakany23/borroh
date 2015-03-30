# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20150330_2103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image_set',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to=b'product_images', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='points_price',
            field=models.IntegerField(max_length=40, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
