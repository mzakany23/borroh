# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'product_images')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_code', models.CharField(max_length=100, null=True, blank=True)),
                ('title', models.CharField(max_length=40)),
                ('description', models.TextField(max_length=1000)),
                ('price', models.CharField(max_length=40)),
                ('slug', models.SlugField(null=True, blank=True)),
                ('discount', models.CharField(blank=True, max_length=40, null=True, choices=[(b'15%', b'15%'), (b'20%', b'20%'), (b'25%', b'25%')])),
                ('points_price', models.CharField(max_length=40, null=True, blank=True)),
                ('borrohed', models.BooleanField(default=False)),
                ('sold', models.BooleanField(default=False)),
                ('status', models.CharField(blank=True, max_length=40, null=True, choices=[(b'New', b'New'), (b'Featured', b'Featured'), (b'Regular', b'Regular')])),
                ('brand', models.CharField(max_length=40, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(to='product.Category', null=True, blank=True)),
                ('image_set', models.ManyToManyField(to='product.Image', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VariantSelection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='variant',
            name='options',
            field=models.ManyToManyField(to='product.VariantSelection'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='variants',
            field=models.ManyToManyField(to='product.Variant', null=True, blank=True),
            preserve_default=True,
        ),
    ]
