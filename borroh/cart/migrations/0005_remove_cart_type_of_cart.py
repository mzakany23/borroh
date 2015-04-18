# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_cart_type_of_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='type_of_cart',
        ),
    ]
