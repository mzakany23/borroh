# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_remove_variant_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.CharField(blank=True, max_length=40, null=True, choices=[(b'15%', b'15%'), (b'20%', b'20%'), (b'25%', b'25%'), (None, None)]),
            preserve_default=True,
        ),
    ]
