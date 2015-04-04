# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20150330_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='image',
            name='product',
            field=models.ForeignKey(blank=True, to='product.Product', null=True),
            preserve_default=True,
        ),
    ]
