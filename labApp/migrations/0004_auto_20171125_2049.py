# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 17:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('labApp', '0003_auto_20171125_1955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usluga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='zakaz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('Usluga', models.CharField(max_length=255, null=True)),
                ('price', models.FloatField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='prodact',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='sex',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Prodact',
        ),
        migrations.AddField(
            model_name='usluga',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labApp.Customer'),
        ),
        migrations.AddField(
            model_name='usluga',
            name='user_zakaz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labApp.zakaz'),
        ),
    ]
