# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20150404_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ManyToManyField(to='product.Image', null=True, blank=True),
            preserve_default=True,
        ),
    ]
