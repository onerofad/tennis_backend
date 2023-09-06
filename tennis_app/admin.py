from django.contrib import admin
from .models import Signup, PlayerRanking

admin.site.register({Signup, PlayerRanking})