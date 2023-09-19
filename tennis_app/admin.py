from django.contrib import admin
from .models import Signup, PlayerRanking, UploadImages, UploadTournamentVideos, UploadHighlightVideos, UploadTeamVideos

admin.site.register({Signup, PlayerRanking, UploadImages, UploadTournamentVideos, UploadHighlightVideos, UploadTeamVideos})