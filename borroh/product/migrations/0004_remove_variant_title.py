# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20150330_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variant',
            name='title',
        ),
    ]
