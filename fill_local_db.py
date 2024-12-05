import os
from pathlib import Path
from sqlite3 import DatabaseError
import yfinance as yf
import logging

logger = logging.getLogger('main_logger')

print(Path(__file__).resolve().parent.parent)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'currency_exchange.settings')

import django

django.setup()

from main.models import CurrencyRate, Currency
from utils.data_processing import DataProcessing
from django.utils import timezone

init_currencies = {'PLN': 'Europe', 'USD': 'North America', 'EUR': 'Europe', 'JPY': 'Asia'}
for currency_code, continent in init_currencies.items():
    new_currency, created = Currency.objects.get_or_create(currency_code=currency_code, continent=continent)
    if not created:
        logger.debug(f'Currency code {currency_code} already present in DB')
        continue
    try:
        new_currency.save()
    except DatabaseError as err:
        logger.error(f'Encountered error on DB site, {err}')

currencies_pairs = DataProcessing.currencies_pair_preparation(init_currencies.keys())
print(currencies_pairs)
tickers = yf.Tickers(currencies_pairs)
for pair in currencies_pairs:
    data_to_send = tickers.history()['Close'][pair]
    bulk_exchange_rate = []
    # format data to aware time
    timestamp_from_ticker = [timezone.make_aware(timestamp) for timestamp in data_to_send.index.tolist()]
    print(f'Handling pair {pair}')
    currencies = Currency.objects.filter(currency_code__in=[pair[:3], pair[3:6]])
    for index, date in enumerate(timestamp_from_ticker):
        existing_exchange_rate = CurrencyRate.objects.filter(date=date, currency1=currencies[0],
                                                             currency2=currencies[1])
        if existing_exchange_rate:
            print(
                f'Exchange rate for {currencies[0]} and {currencies[1]} for date {date} is already present in the DB, '
                f'validating if inverse pair present')
            existing_exchange_rate_reversed = CurrencyRate.objects.filter(date=date, currency1=currencies[1],
                                                                          currency2=currencies[0])
            if existing_exchange_rate_reversed:
                print(
                    f'Exchange rate for {currencies[0]} and {currencies[1]} and inverse pair is present')
            else:
                currencies_pairs_to_send_reversed = CurrencyRate(currency1=currencies[1], currency2=currencies[0],
                                                    exchange_rate=data_to_send.iloc[index], date=date)
                bulk_exchange_rate.append(currencies_pairs_to_send_reversed)
        else:
            currencies_pairs_to_send = CurrencyRate(currency1=currencies[0], currency2=currencies[1],
                                                    exchange_rate=data_to_send.iloc[index], date=date)
            bulk_exchange_rate.append(currencies_pairs_to_send)
    try:
        CurrencyRate.objects.bulk_create(bulk_exchange_rate)

    except DatabaseError:
        logger.error('Error while sending bulk exchange rate')
