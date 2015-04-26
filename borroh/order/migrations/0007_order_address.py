# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0021_usercreditcard_profile'),
        ('order', '0006_auto_20150418_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.ManyToManyField(to='account.Address', null=True, blank=True),
            preserve_default=True,
        ),
    ]
