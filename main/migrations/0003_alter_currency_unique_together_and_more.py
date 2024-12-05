# Generated by Django 5.1.3 on 2024-12-04 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_currency_currency_id'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='currency',
            unique_together={('currency_code', 'continent')},
        ),
        migrations.AlterUniqueTogether(
            name='currencyrate',
            unique_together={('currency1', 'currency2')},
        ),
    ]