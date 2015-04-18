# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0026_auto_20150409_1956'),
        ('order', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0013_address_zip_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='BorrowedInventory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_order_completion', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField(null=True, blank=True)),
                ('order', models.ForeignKey(blank=True, to='order.Order', null=True)),
                ('product', models.ManyToManyField(to='product.Product', null=True, blank=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(blank=True, max_length=40, null=True, choices=[(b'OHIO', b'OHIO')]),
            preserve_default=True,
        ),
    ]
