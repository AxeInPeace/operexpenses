# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-31 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputforms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pathcard',
            name='closed',
            field=models.BooleanField(default=False),
        ),
    ]
