# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20150418_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_order_started',
            field=models.DateField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
    ]
