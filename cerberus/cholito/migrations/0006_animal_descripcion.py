# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 05:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cholito', '0005_usuarionormal_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='descripcion',
            field=models.CharField(default='', max_length=600),
            preserve_default=False,
        ),
    ]