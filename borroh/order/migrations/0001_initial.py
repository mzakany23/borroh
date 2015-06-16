# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('account', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(blank=True, max_length=40, null=True, choices=[(b'started', b'started'), (b'pending', b'pending'), (b'shipped', b'shipped'), (b'done', b'done'), (b'cancel', b'cancel')])),
                ('type_of_cart', models.CharField(blank=True, max_length=40, null=True, choices=[(b'Buy', b'Buy'), (b'Borroh', b'Borroh')])),
                ('date_order_started', models.DateField(auto_now_add=True, null=True)),
                ('free_shipping', models.BooleanField(default=False)),
                ('address', models.ForeignKey(blank=True, to='account.Address', null=True)),
                ('cart', models.ForeignKey(blank=True, to='cart.Cart', null=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
