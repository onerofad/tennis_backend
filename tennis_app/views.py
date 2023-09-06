from django.shortcuts import render
from rest_framework import viewsets
from .models import Signup
from .serializers import SignupSerializer

class SignupView(viewsets.ModelViewSet):
    queryset = Signup.objects.all()
    serializer_class = SignupSerializer


