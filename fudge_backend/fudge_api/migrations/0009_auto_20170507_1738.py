# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 17:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fudge_api', '0008_auto_20170507_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transaction', to='fudge_api.Category'),
        ),
    ]
