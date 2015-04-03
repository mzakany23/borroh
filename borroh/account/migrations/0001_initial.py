# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0008_auto_20150330_2140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profile_pic', models.ImageField(upload_to=b'profile_pics')),
                ('street', models.CharField(max_length=40, null=True, blank=True)),
                ('city', models.CharField(max_length=40, null=True, blank=True)),
                ('state', models.CharField(max_length=40, null=True, blank=True)),
                ('zip', models.CharField(max_length=40, null=True, blank=True)),
                ('favorites', models.ManyToManyField(to='product.Product', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='account',
            name='profile',
            field=models.OneToOneField(null=True, blank=True, to='account.Profile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
