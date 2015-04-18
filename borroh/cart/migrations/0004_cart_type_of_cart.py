# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20150410_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='type_of_cart',
            field=models.CharField(blank=True, max_length=40, null=True, choices=[(b'Buy', b'Buy'), (b'Borroh', b'Borroh')]),
            preserve_default=True,
        ),
    ]
