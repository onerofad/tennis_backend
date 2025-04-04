from django.db import models
import random

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    #return randint(range_start, range_end)

def getRandom():
    random_number = random.randint(1000000000, 9999999999)
    return random_number

class Register(models.Model):
    fname = models.CharField(max_length=255, default="")
    lname = models.CharField(max_length=255, default="")
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, default="")
    dob = models.TextField(max_length=255, default='')
    password = models.CharField(max_length=255)
    verify = models.IntegerField(default=0)
    email_notification = models.CharField(default="0", max_length=255)
    text_notification = models.CharField(default="0", max_length=255)

    def __str__(self):
        return self.email

class ExchangeRates(models.Model):
    country = models.CharField(max_length = 255)
    countrycode = models.CharField(max_length = 255)
    rate = models.FloatField()
    fee = models.IntegerField(default = 0)

    def __str__(self):
        return self.country
    
class Transactions(models.Model):
    moneySent = models.FloatField()
    moneyReceived = models.FloatField()
    currencySent = models.CharField(max_length = 255, default = '')
    currencyReceived = models.CharField(max_length = 255, default = '' )
    fee = models.FloatField()
    total = models.FloatField()

    deliveryBank = models.BooleanField(default = False)
    deliveryCash = models.BooleanField(default = False)
    bankname = models.CharField(max_length = 255, default = "")

    accountNumber = models.CharField(max_length = 255)
    retypeAccountNumber = models.CharField(max_length = 255)
    checking = models.BooleanField(default = False)
    savings = models.BooleanField(default = False)

    fname = models.CharField(max_length = 255)
    mname = models.CharField(max_length = 255, default = 'none')
    lname = models.CharField(max_length = 255)
    slname = models.CharField(max_length = 255, default = 'none')
    country = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    street = models.CharField(max_length = 255)
    street2 = models.CharField(max_length = 255, default = 'none' )
    region = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    postal = models.CharField(max_length = 255)

    cardNumber = models.CharField(max_length = 255)
    expiration = models.CharField(max_length = 255)
    securityCode = models.CharField(max_length = 255)
    b_fname = models.CharField(max_length = 255)
    nickname = models.CharField(max_length = 255, default = 'none') 
    streetAd = models.CharField(max_length = 255)
    apartment = models.CharField(max_length = 255,  default = 'none')
    b_city = models.CharField(max_length = 255)
    b_region = models.CharField(max_length = 255)
    zipcode = models.CharField(max_length = 255)

    senderEmail = models.CharField(max_length = 255, default = '')
    trans_date = models.DateField(auto_now = True)

    status = models.CharField(max_length=255, default='Pending')
    trans_id = models.CharField(max_length=255, default=getRandom())

    moneyRate = models.FloatField(default=0)
    currencySentLabel = models.CharField(max_length=255, default='')
    currencyReceivedLabel = models.CharField(max_length=255, default='')

class PaymentMethod(models.Model):
    cardNumber = models.CharField(max_length = 255)
    expiration = models.CharField(max_length = 255)
    securityCode = models.CharField(max_length = 255)
    b_fname = models.CharField(max_length = 255)
    nickname = models.CharField(max_length = 255) 
    streetAd = models.CharField(max_length = 255)
    apartment = models.CharField(max_length = 255)
    b_city = models.CharField(max_length = 255)
    b_region = models.CharField(max_length = 255)
    zipcode = models.CharField(max_length = 255)
    email = models.CharField(max_length= 255, default="")

    def __str__(self):
        return self.cardNumber

class Country(models.Model):
    label = models.CharField(max_length=255, default="")
    value = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.label

    
class BankInfo(models.Model):
    bank_name = models.CharField(max_length=255)
    bank_image = models.TextField(default="")

    def __str__(self):
        return self.bank_name
    
class Recepients(models.Model):
    fname = models.CharField(max_length = 255)
    mname = models.CharField(max_length = 255, default = "none")
    lname = models.CharField(max_length = 255)
    slname = models.CharField(max_length = 255, default = "none")
    country = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    street = models.CharField(max_length = 255)
    street2 = models.CharField(max_length = 255, default = "none")
    region = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    postal = models.CharField(max_length = 255)
    account_email = models.CharField(max_length= 255, default="")

    def __str__(self):
        return self.fname
    
class TemporaryTransactions(models.Model):
    moneySent = models.FloatField(default='')
    moneyReceived = models.FloatField(default='')
    currencySent = models.CharField(max_length = 255, default = '')
    currencyReceived = models.CharField(max_length = 255, default = '' )
    fee = models.FloatField(default='')
    total = models.FloatField(default='')

    deliveryBank = models.BooleanField(default = False)
    deliveryCash = models.BooleanField(default = False)
    bankname = models.CharField(max_length = 255, default = "")

    accountNumber = models.CharField(max_length = 255, default = "" )
    retypeAccountNumber = models.CharField(max_length = 255, default = "")
    checking = models.BooleanField(default = False)
    savings = models.BooleanField(default = False)

    fname = models.CharField(max_length = 255, default = '')
    mname = models.CharField(max_length = 255, default = 'none')
    lname = models.CharField(max_length = 255, default = '')
    slname = models.CharField(max_length = 255, default = 'none')
    country = models.CharField(max_length = 255, default = '')
    email = models.CharField(max_length = 255, default = '')
    street = models.CharField(max_length = 255, default = 'none')
    street2 = models.CharField(max_length = 255, default = '' )
    region = models.CharField(max_length = 255, default='')
    city = models.CharField(max_length = 255, default='')
    postal = models.CharField(max_length = 255, default='')

    cardNumber = models.CharField(max_length = 255, default='')
    expiration = models.CharField(max_length = 255, default='')
    securityCode = models.CharField(max_length = 255, default='')
    b_fname = models.CharField(max_length = 255, default='')
    nickname = models.CharField(max_length = 255, default = 'none') 
    streetAd = models.CharField(max_length = 255, default='')
    apartment = models.CharField(max_length = 255,  default = 'none')
    b_city = models.CharField(max_length = 255, default='')
    b_region = models.CharField(max_length = 255, default='')
    zipcode = models.CharField(max_length = 255, default='')
    emailId = models.CharField(max_length = 255, default='')
    moneyRate = models.FloatField(default=0)
    currencySentLabel = models.CharField(max_length=255, default='')
    currencyReceivedLabel = models.CharField(max_length=255, default='')
    trans_id = models.CharField(max_length=255, default=getRandom())

class SilaUser(models.Model):
  user_handle = models.CharField(max_length=255) 
  password = models.CharField(max_length=255, default="")
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  entity_name = models.CharField(max_length=255)
  birthdate = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  phone = models.CharField(max_length=255)
  identity_value = models.CharField(max_length=255)
  street_address_1 = models.CharField(max_length=255)
  street_address_2 = models.CharField(max_length=255, default="None")
  city = models.CharField(max_length=255)
  state = models.CharField(max_length=255)
  country = models.CharField(max_length=255)
  postal_code = models.TextField(default='')



    