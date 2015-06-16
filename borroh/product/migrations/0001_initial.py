# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40)),
                ('gender', models.CharField(blank=True, max_length=40, null=True, choices=[(b'Male', b'Male'), (b'Female', b'Female'), (b'Unisex', b'Unisex')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('category', models.ManyToManyField(to='product.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('default', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to=b'product_images')),
                ('zoom_image', models.BooleanField(default=False)),
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
                ('slug', models.SlugField(null=True, blank=True)),
                ('borrohed', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False)),
                ('sold', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=40)),
                ('description', models.TextField(max_length=1000, null=True, blank=True)),
                ('price', models.DecimalField(default=0.0, max_digits=10, decimal_places=2)),
                ('points_price', models.IntegerField(default=0, max_length=40, null=True, blank=True)),
                ('gender', models.CharField(blank=True, max_length=40, null=True, choices=[(b'Male', b'Male'), (b'Female', b'Female'), (b'Unisex', b'Unisex')])),
                ('discount', models.CharField(blank=True, max_length=40, null=True, choices=[(b'15%', b'15%'), (b'20%', b'20%'), (b'25%', b'25%'), (None, None)])),
                ('status', models.CharField(blank=True, max_length=40, null=True, choices=[(b'New', b'New'), (b'Regular', b'Regular')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('brand', models.ManyToManyField(to='product.Brand', null=True, blank=True)),
                ('category', models.ManyToManyField(to='product.Category', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SizeCollection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('size', models.ManyToManyField(to='product.Size')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ForeignKey(blank=True, to='product.SizeCollection', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='image',
            name='product',
            field=models.ForeignKey(blank=True, to='product.Product', null=True),
            preserve_default=True,
        ),
    ]
