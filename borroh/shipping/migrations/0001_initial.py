# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_remove_order_shipping'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('carrier', models.CharField(max_length=40)),
                ('carrier_account_id', models.CharField(max_length=40)),
                ('buyer_address_id', models.CharField(max_length=40)),
                ('seller_address_id', models.CharField(max_length=40)),
                ('rate', models.CharField(max_length=40)),
                ('service', models.CharField(max_length=40)),
                ('tracking_code', models.CharField(max_length=40, null=True, blank=True)),
                ('estimated_delivery_days', models.CharField(max_length=40, null=True, blank=True)),
                ('order', models.ForeignKey(to='order.Order')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
