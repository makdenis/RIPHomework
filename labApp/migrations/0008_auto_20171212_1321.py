# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-12 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labApp', '0007_auto_20171207_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
