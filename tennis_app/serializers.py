from rest_framework import serializers
from .models import Signup, PlayerRanking

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        fields = ('id', 'fname', 'lname', 'dob', 'email', 'password', 'nationality', 'handbat')

class PlayerRankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        fields = ('id', 'first_name', 'last_name', 'points')