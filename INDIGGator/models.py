from pyexpat import model
from statistics import mode
from django.db import models
import random

# Create your models here.



class User(models.Model):
    userName = models.CharField(max_length=255,null=False,blank=False)
    walletAddress = models.CharField(max_length=255,null=False,blank=False)
    whoReferedMe = models.CharField(max_length=255,null=True,blank=True)
    myRefrealCode = models.CharField(max_length=255,null=True,blank=True)
    isKycVerified = models.BooleanField(default=False,null=True)

    def __str__(self):
        return self.walletAddress
 
