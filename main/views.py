from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
import django_filters
from .serializers import CurrencySerializer, CurrencyRateSerializer
from .models import CurrencyRate, Currency

# Create your views here.

# from currency_exchange.main.models import CurrencyRate


class CurrencyFilter(django_filters.FilterSet):
    currency1 = django_filters.CharFilter(field_name='currency1__currency_code', lookup_expr='exact')
    currency2 = django_filters.CharFilter(field_name='currency2__currency_code', lookup_expr='exact')


    class Meta:
        model = CurrencyRate
        fields = ['currency1', 'currency2']


class CurrenciesView(generics.ListAPIView):
    queryset = Currency.objects.all().order_by('continent')
    serializer_class = CurrencySerializer


class CurrencyRateView(generics.ListAPIView):
    queryset = CurrencyRate.objects.all()
    serializer_class = CurrencyRateSerializer
    permission_classes = [IsAdminUser]


class LatestExchangeRate(APIView):
    def get(self, request, currency1, currency2):
        try:
            latest_exchange_rate = CurrencyRate.objects.filter(currency1__currency_code=currency1.upper(), currency2__currency_code=currency2.upper()).order_by('-date').first()
            if latest_exchange_rate:
                return Response(CurrencyRateSerializer(latest_exchange_rate).data, status=status.HTTP_200_OK)
            else:
                return Response(f'Could not find records for currencies {currency1} and {currency2} in local DB', status=status.HTTP_404_NOT_FOUND)
        except CurrencyRate.DoesNotExist:
            return Response({'Could not get results from DB'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class FilterCurrencies(generics.ListAPIView):
    # url should look like this i.e. filter_currencies/?currency1=PLN&currency2=EUR
    queryset = CurrencyRate.objects.all()
    serializer_class = CurrencyRateSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_class = CurrencyFilter
    