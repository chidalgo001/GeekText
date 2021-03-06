# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-08 05:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('books', '0004_book_pages'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='birthplace',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='description',
            field=models.TextField(blank=True, max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='education',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='website',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
