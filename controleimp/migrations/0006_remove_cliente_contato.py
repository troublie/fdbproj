# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 19:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controleimp', '0005_auto_20171117_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='contato',
        ),
    ]
