# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_image_default'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='gender',
            field=models.CharField(blank=True, max_length=40, null=True, choices=[(b'Male', b'Male'), (b'Female', b'Female'), (b'Unisex', b'Unisex')]),
            preserve_default=True,
        ),
    ]
