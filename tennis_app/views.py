from django.shortcuts import render
from rest_framework import viewsets
from .models import Signup, PlayerRanking, UploadImages
from .serializers import SignupSerializer, PlayerRankingSerializer, UploadImagesSerializer

class SignupView(viewsets.ModelViewSet):
    queryset = Signup.objects.all().order_by("-points")
    serializer_class = SignupSerializer

class PlayerRankingView(viewsets.ModelViewSet):
    queryset = PlayerRanking.objects.all().order_by("-points")
    serializer_class = PlayerRankingSerializer

class UploadImagesView(viewsets.ModelViewSet):
    queryset = UploadImages.objects.all()
    serializer_class = UploadImagesSerializer


