# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20150330_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, max_length=40, null=True, choices=[(b'SM', b'SM'), (b'MD', b'MD'), (b'LG', b'LG')]),
            preserve_default=True,
        ),
    ]
