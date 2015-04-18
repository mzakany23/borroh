# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_auto_20150418_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrowedinventory',
            name='order',
        ),
        migrations.RemoveField(
            model_name='borrowedinventory',
            name='product',
        ),
        migrations.RemoveField(
            model_name='borrowedinventory',
            name='user',
        ),
        migrations.DeleteModel(
            name='BorrowedInventory',
        ),
    ]
