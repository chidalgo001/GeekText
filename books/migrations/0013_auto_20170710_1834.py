# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 22:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('books', '0012_auto_20170710_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]