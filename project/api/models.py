from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class Admin(models.Model):
    advisor_name = models.CharField(max_length=50,blank=False,null=False)
    advisor_pic_url = models.URLField(max_length=200,null=False,blank=False)

class UserModel(models.Model):
    u_name = models.CharField( max_length=50, blank=False,null=False)
    email = models.EmailField( max_length=254, blank=False,null=False)
    password = models.CharField(max_length=50,blank=False,null= False)
