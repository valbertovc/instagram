# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-15 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='legenda',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]