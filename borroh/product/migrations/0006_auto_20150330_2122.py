# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20150330_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variant',
            name='options',
        ),
        migrations.DeleteModel(
            name='VariantSelection',
        ),
        migrations.RemoveField(
            model_name='product',
            name='variants',
        ),
        migrations.DeleteModel(
            name='Variant',
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, max_length=40, null=True, choices=[(b'New', b'New'), (b'Featured', b'Featured'), (b'Regular', b'Regular')]),
            preserve_default=True,
        ),
    ]
