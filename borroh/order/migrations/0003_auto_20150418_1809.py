# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20150418_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, max_length=40, null=True, choices=[(b'pending', b'pending'), (b'shipped', b'shipped'), (b'done', b'done'), (b'cancel', b'cancel')]),
            preserve_default=True,
        ),
    ]
