# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, null=True, blank=True)),
                ('free_shipments', models.IntegerField(default=0)),
                ('own_it_discount', models.DecimalField(default=0.0, max_digits=10, decimal_places=2)),
                ('points_per_month', models.IntegerField(default=0)),
                ('price_per_month', models.DecimalField(default=0.0, max_digits=10, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
