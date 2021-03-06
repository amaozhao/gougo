# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 07:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('price', models.IntegerField(verbose_name='price')),
                ('description', models.TextField(verbose_name='description')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated time')),
                ('image', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_images', to='filer.Image')),
            ],
            options={
                'ordering': ['-created'],
                'db_table': 'item',
                'verbose_name': 'item',
                'verbose_name_plural': 'items',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.IntegerField(verbose_name='money')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='gou.Item', verbose_name='item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='item')),
            ],
            options={
                'ordering': ['-created'],
                'db_table': 'order',
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
            },
        ),
    ]
