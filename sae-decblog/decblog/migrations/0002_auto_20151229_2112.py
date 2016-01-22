# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-29 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(default=b'uname', max_length=256),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(blank=True, default=b'new-post', max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.CharField(blank=True, default=b'uname', max_length=256, null=True),
        ),
    ]
