# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20150616_1657'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='borroh',
            new_name='borrohcount',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='buy',
            new_name='buycount',
        ),
    ]
