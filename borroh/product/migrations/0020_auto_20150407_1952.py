# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_size_sizecollection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.OneToOneField(null=True, blank=True, to='product.SizeCollection'),
            preserve_default=True,
        ),
    ]
