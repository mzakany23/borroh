# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0020_usercreditcard_card_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercreditcard',
            name='profile',
            field=models.ForeignKey(blank=True, to='account.Profile', null=True),
            preserve_default=True,
        ),
    ]
