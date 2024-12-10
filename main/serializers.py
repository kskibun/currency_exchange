from rest_framework import serializers
from .models import Currency, CurrencyRate



class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['continent', 'currency_code']


class CurrencyRateSerializer(serializers.ModelSerializer):
    currency1 = serializers.CharField(read_only=True, source='currency1.currency_code')
    currency2 = serializers.CharField(read_only=True, source='currency2.currency_code')

    class Meta:
        model = CurrencyRate
        fields = ['currency1', 'currency2', 'exchange_rate', 'date']

