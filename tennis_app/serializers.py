from rest_framework import serializers
from .models import Signup

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        fields = ('id', 'fname', 'lname', 'dob', 'email', 'password', 'nationality', 'handbat')

