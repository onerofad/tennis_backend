from django.db import models

class Signup (models.Model):
    fname = models.CharField(max_length=255, unique=True)
    lname = models.CharField(max_length=255, unique=True)
    dob =   models.DateField()
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255, default="")
    nationality = models.CharField(max_length=255, default="")
    handbat = models.CharField(max_length=255, default="")

class PlayerRanking (models.Model):
    first_name = models.ForeignKey(Signup, on_delete=models.CASCADE, to_field="fname", related_name='first_name')
    last_name = models.ForeignKey(Signup, on_delete=models.CASCADE, to_field="lname", related_name='last_name')
    points = models.IntegerField()





    def __str__(self):
        return self.fname


