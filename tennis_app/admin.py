from django.contrib import admin
from .models import Register, ExchangeRates, Transactions, PaymentMethod, BankInfo, Recepients, TemporaryTransactions, Country

admin.site.register({Register, ExchangeRates, Transactions, PaymentMethod, BankInfo, Recepients, TemporaryTransactions, Country})