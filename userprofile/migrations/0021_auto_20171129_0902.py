# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 09:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0020_about_us_scholar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about_us',
            old_name='img',
            new_name='Image',
        ),
        migrations.AddField(
            model_name='about_us',
            name='sync',
            field=models.CharField(default='1', max_length=200),
            preserve_default=False,
        ),
    ]
