# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0002_auto_20150416_2010'),
        ('account', '0008_auto_20150416_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='subscription',
            field=models.ForeignKey(blank=True, to='subscription.Subscription', null=True),
            preserve_default=True,
        ),
    ]
