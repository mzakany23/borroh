# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20150410_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineitem',
            name='cart',
            field=models.ForeignKey(to='cart.Cart'),
            preserve_default=True,
        ),
    ]
