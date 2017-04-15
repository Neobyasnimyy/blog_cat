# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 23:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('post_image', models.ImageField(upload_to='products_images/')),
                ('post_created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('post_published_date', models.DateTimeField(blank=True, null=True)),
                ('post_likes', models.IntegerField()),
            ],
            options={
                'db_table': 'post',
            },
        ),
    ]
