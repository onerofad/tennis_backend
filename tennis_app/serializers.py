from rest_framework import serializers
from .models import Signup, PlayerRanking, UploadImages, UploadTournamentVideos, UploadHighlightVideos

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        fields = ('id', 'fname', 'lname', 'dob', 'email', 'password', 'nationality', 'handbat', "imageurl", "currenteam", "lastchamp", "datelastchamp", "locatelastchamp", "favoriteplayer", "points")

class PlayerRankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerRanking
        fields = ('id', 'firstname', 'leaguetype', 'points')

class UploadImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadImages
        fields = ("id", "title", "imageurl")

class UploadTournamentVideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadTournamentVideos
        fields = ("id", "videodescription" ,"videourl")

class UploadHighlightVideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadHighlightVideos
        fields = ("id", "videodescription" ,"videourl")
