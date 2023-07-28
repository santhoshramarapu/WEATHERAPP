from django.db import models
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class BaseUserManger(models.Model):
     username = models.CharField(max_length=100, null=True)
     password = models.CharField(max_length=150, null=True)
    


     class Meta:
        db_table ='dbusername'
         

     def __str__(self):
        return self.name



