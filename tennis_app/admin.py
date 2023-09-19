from django.contrib import admin
from .models import Signup, PlayerRanking, UploadImages, uploadVideos

admin.site.register({Signup, PlayerRanking, UploadImages, uploadVideos})