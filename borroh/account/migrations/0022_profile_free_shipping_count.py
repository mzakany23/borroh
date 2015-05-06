# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0021_usercreditcard_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='free_shipping_count',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
