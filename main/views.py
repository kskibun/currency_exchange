from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

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
            currency1_code = Currency.objects.get(currency_code__iexact=currency1)
            currency2_code = Currency.objects.get(currency_code__iexact=currency2)
            latest_exchange_rate = CurrencyRate.objects.filter(currency1_id=currency1_code.id, currency2_id=currency2_code.id).order_by('-date').first()
            if currency2_code or currency1_code:
                return Response(CurrencyRateSerializer(latest_exchange_rate).data, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "after latest rate"}, status=status.HTTP_404_NOT_FOUND)
        except CurrencyRate.DoesNotExist:
            return Response({"detail": "Exchange rate not found."}, status=status.HTTP_404_NOT_FOUND)
