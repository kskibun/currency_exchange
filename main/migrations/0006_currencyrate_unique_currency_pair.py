# Generated by Django 5.1.3 on 2024-12-05 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_currency_unique_together'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='currencyrate',
            constraint=models.UniqueConstraint(fields=('currency1', 'currency2'), name='unique_currency_pair'),
        ),
    ]
