# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0021_usercreditcard_profile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0005_remove_cart_type_of_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(blank=True, max_length=40, null=True, choices=[(b'started', b'started'), (b'pending', b'pending'), (b'shipped', b'shipped'), (b'done', b'done'), (b'cancel', b'cancel')])),
                ('type_of_cart', models.CharField(blank=True, max_length=40, null=True, choices=[(b'Buy', b'Buy'), (b'Borroh', b'Borroh')])),
                ('date_order_started', models.DateField(auto_now_add=True, null=True)),
                ('shipping', models.CharField(default=b'road', max_length=40, choices=[(b'road', b'road'), (b'air', b'air')])),
                ('address', models.ForeignKey(blank=True, to='account.Address', null=True)),
                ('cart', models.ForeignKey(blank=True, to='cart.Cart', null=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
