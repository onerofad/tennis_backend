from rest_framework import serializers
from .models import Register, ExchangeRates, Transactions, PaymentMethod, BankInfo, Recepients, TemporaryTransactions, Country

import json

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Register

class ExchangeRatesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ExchangeRates

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Transactions

class RecepientSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Transactions

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = PaymentMethod

class BankInfoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = BankInfo

class RecepientSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Recepients

class TemporaryTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = TemporaryTransactions

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Country


      