from .models import Register, ExchangeRates, Transactions, PaymentMethod, BankInfo, Recepients, TemporaryTransactions, Country
from .serializers import RegisterSerializer, ExchangeRatesSerializer, TransactionSerializer, PaymentMethodSerializer, BankInfoSerializer, RecepientSerializer, TemporaryTransactionSerializer, CountrySerializer
from rest_framework import viewsets
from datetime import date

class RegisterView(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

class ExchangeRatesView(viewsets.ModelViewSet):
    queryset = ExchangeRates.objects.all()
    serializer_class = ExchangeRatesSerializer

class TransactionView(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer

class RecentTransactionView(viewsets.ModelViewSet):
    queryset = Transactions.objects.filter(trans_date = date.today())
    serializer_class = TransactionSerializer

class RecepientView(viewsets.ModelViewSet):
    queryset = Recepients.objects.all()
    serializer_class = RecepientSerializer


class PaymentMethodView(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer

class BankInfoView(viewsets.ModelViewSet):
    queryset = BankInfo.objects.all()
    serializer_class = BankInfoSerializer

class TemporaryTransactionView(viewsets.ModelViewSet):
    queryset = TemporaryTransactions.objects.all()
    serializer_class = TemporaryTransactionSerializer

class CountryView(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
