# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_auto_20150424_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercreditcard',
            name='card_token',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
    ]
