# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_auto_20150424_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCreditCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('credit_card_last_4', models.CharField(max_length=4)),
                ('type_of_credit_card', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='profile',
            name='zip',
        ),
    ]
