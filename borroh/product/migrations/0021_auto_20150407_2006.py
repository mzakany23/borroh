# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_auto_20150407_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ForeignKey(blank=True, to='product.SizeCollection', null=True),
            preserve_default=True,
        ),
    ]
