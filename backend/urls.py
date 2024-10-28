"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tennis_app.views import RegisterView, ExchangeRatesView, TransactionView, PaymentMethodView, BankInfoView, RecepientView, TemporaryTransactionView, CountryView, RecentTransactionView, SilaUserView
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('register', RegisterView, 'register')
router.register('rates', ExchangeRatesView, 'rate')
router.register('transactions', TransactionView, 'transaction')
router.register('recent_transactions', RecentTransactionView, 'recent_transaction')
router.register('paymentmethod', PaymentMethodView, 'paymentmethods')
router.register('bankinfo', BankInfoView, 'bankinformation')
router.register('recepients', RecepientView, 'recepient')
router.register('temporary_transactions', TemporaryTransactionView, 'temporary_transaction')
router.register('country', CountryView, 'countries')
router.register('sila_users', SilaUserView, 'sila_user')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
