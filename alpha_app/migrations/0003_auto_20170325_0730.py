# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-03-25 07:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alpha_app', '0002_auto_20170325_0728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='customer',
        ),
    ]