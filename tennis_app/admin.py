from django.contrib import admin
from .models import Signup, PlayerRanking, UploadImages, UploadTournamentVideos

admin.site.register({Signup, PlayerRanking, UploadImages, UploadTournamentVideos})