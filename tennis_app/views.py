from django.shortcuts import render
from rest_framework import viewsets
from .models import Signup
from .serializers import SignupSerializer, PlayerRankingSerializer

class SignupView(viewsets.ModelViewSet):
    queryset = Signup.objects.all()
    serializer_class = SignupSerializer

class PlayerRankingView(viewsets.ModelViewSet):
    queryset = Signup.objects.all()
    serializer_class = PlayerRankingSerializer


