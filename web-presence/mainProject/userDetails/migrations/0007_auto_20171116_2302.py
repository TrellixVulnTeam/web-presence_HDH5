# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-16 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userDetails', '0006_memberdetails_memberurlusername'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberdetails',
            name='memberURLUserName',
            field=models.CharField(max_length=15, verbose_name='User Name'),
        ),
    ]
