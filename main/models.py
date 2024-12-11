from django.db import models

# Create your models here.


class Currency(models.Model):
    continent = models.CharField(max_length=10)
    currency_code = models.CharField(max_length=3, unique=True)


    def __str__(self):
        return self.currency_code


class CurrencyRate(models.Model):
    currency1 = models.ForeignKey(Currency, on_delete=models.DO_NOTHING, related_name='currency1')
    currency2 = models.ForeignKey(Currency, on_delete=models.DO_NOTHING, related_name='currency2')
    exchange_rate = models.FloatField(max_length=7)
    date = models.DateTimeField()
