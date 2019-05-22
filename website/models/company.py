from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255, null= True)
    code = models.BigIntegerField(default="0")
    location = models.CharField(max_length=255, null= True)
    owner = models.CharField(max_length=255)
    character= models.CharField(max_length=255)