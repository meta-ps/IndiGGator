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
    isKycVerified = models.CharField(max_length=255,null=True,blank=True,default="False")

    def __str__(self):
        return self.walletAddress
 
class KYCData(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    FullName = models.CharField(max_length=255,null=False,blank=False)
    IdNumber= models.CharField(max_length=255,null=False,blank=False)
    documentFile = models.FileField(upload_to = 'Files/')
    image = models.ImageField(upload_to='images/',blank=True)

    def __str__(self):
        return self.IdNumber
