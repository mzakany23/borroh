# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='points',
            new_name='free_shipments',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='price',
            new_name='own_it_discount',
        ),
        migrations.AddField(
            model_name='subscription',
            name='points_per_month',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subscription',
            name='price_per_month',
            field=models.DecimalField(default=0.0, max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscription',
            name='name',
            field=models.CharField(max_length=40, null=True, blank=True),
            preserve_default=True,
        ),
    ]
