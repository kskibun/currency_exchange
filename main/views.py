from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .serializers import CurrencySerializer, CurrencyRateSerializer
from .models import CurrencyRate, Currency

# Create your views here.


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
