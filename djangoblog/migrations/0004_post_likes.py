# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoblog', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
