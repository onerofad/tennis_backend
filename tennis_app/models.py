from django.db import models
from cloudinary.models import CloudinaryField

class Signup (models.Model):
    fname = models.CharField(max_length=255, unique=True)
    lname = models.CharField(max_length=255, unique=True)
    dob =   models.DateField()
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255, default="")
    nationality = models.CharField(max_length=255, default="")
    handbat = models.CharField(max_length=255, default="")
    imageurl = models.TextField(default="")
    currenteam = models.TextField(default="")
    lastchamp = models.TextField(default="")
    datelastchamp = models.DateField(default="2023-01-01")
    locatelastchamp = models.TextField(default="")
    favoriteplayer = models.TextField(default="")
    

    def __str__(self):
        return self.fname
    
class PlayerRanking(models.Model):
    firstname = models.ForeignKey(Signup, on_delete=models.CASCADE, to_field="fname")
    leaguetype = models.CharField(max_length=255, default="")
    points = models.IntegerField()


    


