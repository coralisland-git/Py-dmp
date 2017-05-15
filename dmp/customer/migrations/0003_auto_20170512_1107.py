# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-12 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='second_name',
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='last name'),
        ),
    ]