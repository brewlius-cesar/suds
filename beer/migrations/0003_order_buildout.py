# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 19:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beer', '0002_beer_as_batch_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('beer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='line_items', to='beer.Beer')),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='packages',
        ),
        migrations.AlterField(
            model_name='order',
            name='date_filled',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_placed',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='line_items', to='beer.Order'),
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='package_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='line_items', to='beer.PackageType'),
        ),
        migrations.AddField(
            model_name='package',
            name='line_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='packages', to='beer.OrderLineItem'),
        ),
    ]