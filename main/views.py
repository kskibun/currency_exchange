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
    currency1 = django_filters.CharFilter(field_name='currency1', lookup_expr='exact')
    currency2 = django_filters.CharFilter(field_name='currency2', lookup_expr='exact')


    class Meta:
        model = CurrencyRate
        fields = ['currency1', 'currency2']

    # get id by code from Currency db
    def filter_queryset(self, queryset):
        currency1_code = self.data.get('currency1')
        currency2_code = self.data.get('currency2')

        if currency1_code:
            currency1_ids = Currency.objects.filter(currency_code=currency1_code).values_list('id', flat=True)
            queryset = queryset.filter(currency1__id__in=currency1_ids)

        if currency2_code:
            currency2_ids = Currency.objects.filter(currency_code=currency2_code).values_list('id', flat=True)
            queryset = queryset.filter(currency2__id__in=currency2_ids)

        return queryset

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
            currency1_code = get_object_or_404(Currency, currency_code__iexact=currency1)
            currency2_code = get_object_or_404(Currency, currency_code__iexact=currency2)
            latest_exchange_rate = CurrencyRate.objects.filter(currency1_id=currency1_code.id, currency2_id=currency2_code.id).order_by('-date').first()
            if latest_exchange_rate:
                return Response(CurrencyRateSerializer(latest_exchange_rate).data, status=status.HTTP_200_OK)
            else:
                return Response(f'Could not find records for currencies {currency1_code} and {currency2_code} in local DB', status=status.HTTP_404_NOT_FOUND)
        except CurrencyRate.DoesNotExist:
            return Response({'Could not get results from DB'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class FilterCurrencies(generics.ListAPIView):
    # url should look like this i.e. filter_currencies/?currency1=PLN&currency2=EUR
    queryset = CurrencyRate.objects.all()
    serializer_class = CurrencyRateSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_class = CurrencyFilter
    