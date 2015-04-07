# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_product_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(blank=True, max_length=40, null=True, choices=[(b'New', b'New'), (b'Regular', b'Regular')]),
            preserve_default=True,
        ),
    ]
