from datetime import datetime

from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from .models import Currency, CurrencyRate
from django.utils import timezone
import time

class CurrencyRateTests(TestCase):
    def setUp(self):
        self.currency1 = Currency.objects.create(currency_code='USD', continent='North America')
        self.currency2 = Currency.objects.create(currency_code='EUR', continent='Europe')
        self.currency_rate = CurrencyRate.objects.create(
            currency1=self.currency1,
            currency2=self.currency2,
            exchange_rate=0,
            date=timezone.make_aware(datetime.now())
        )
        self.reversed_currency_rate = CurrencyRate.objects.create(currency1=self.currency2,
            currency2=self.currency1,
            exchange_rate=0,
            date=timezone.make_aware(datetime.now()))
        self.client = APIClient()

    def test_currency_rate_retrieval_valid_codes(self):
        url = reverse('exchange_rate', kwargs={'currency1': 'USD', 'currency2': 'EUR'})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['currency1'], 'USD')
        self.assertEqual(response.data['currency2'], 'EUR')

    def test_currency_rate_retrieval_invalid_codes(self):

        url = reverse('exchange_rate', args=['USD', 'XYZ'])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_currency_rate_retrieval_reversed_codes(self):
        url = reverse('exchange_rate', kwargs={'currency1': 'EUR', 'currency2': 'USD'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['currency1'], 'EUR')
        self.assertEqual(response.data['currency2'], 'USD')
