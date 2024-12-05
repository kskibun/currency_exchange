# Generated by Django 5.1.3 on 2024-12-03 20:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_id', models.IntegerField()),
                ('continent', models.CharField(max_length=10)),
                ('currency_code', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='CurrencyRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exchange_rate', models.FloatField(max_length=7)),
                ('date', models.DateTimeField()),
                ('currency1', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='currency1', to='main.currency')),
                ('currency2', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='currency2', to='main.currency')),
            ],
        ),
    ]
