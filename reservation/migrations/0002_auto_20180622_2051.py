# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-22 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_phone',
            field=models.CharField(max_length=20),
        ),
    ]
