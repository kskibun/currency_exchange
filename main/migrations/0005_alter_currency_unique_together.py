# Generated by Django 5.1.3 on 2024-12-05 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_currencyrate_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='currency',
            unique_together=set(),
        ),
    ]
