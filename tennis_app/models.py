from django.db import models

class Signup (models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    dob =   models.DateField()
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255, default="")
    nationality = models.CharField(max_length=255, default="")
    handbat = models.CharField(max_length=255, default="")




    def __str__(self):
        return self.fname


