from django.urls import path

from .views import CurrenciesView, CurrencyRateView, LatestExchangeRate, FilterCurrencies

urlpatterns = [
    path("currency/", CurrenciesView.as_view()),
    path("test/", CurrencyRateView.as_view()),
    path('currencies/<str:currency1>/<str:currency2>/', LatestExchangeRate.as_view(), name='exchange_rate'),
    path('filter_currencies/', FilterCurrencies.as_view())
]