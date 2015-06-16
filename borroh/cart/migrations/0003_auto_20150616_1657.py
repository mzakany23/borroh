# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20150616_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='borroh',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cart',
            name='buy',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
