# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controleimp', '0010_pedido_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='data',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]