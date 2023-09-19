from django.contrib import admin
from .models import Signup, PlayerRanking, UploadImages 

admin.site.register({Signup, PlayerRanking, UploadImages})