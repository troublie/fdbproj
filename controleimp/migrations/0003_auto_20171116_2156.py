# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 23:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controleimp', '0002_auto_20171114_1800'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moeda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=3)),
                ('descricao', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TermoPagto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('termo', models.IntegerField(max_length=3)),
            ],
        ),
        migrations.AlterField(
            model_name='pedido',
            name='moeda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controleimp.Moeda'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='termo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controleimp.TermoPagto'),
        ),
    ]