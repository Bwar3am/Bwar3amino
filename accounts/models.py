from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# class users(models.Model):
#     name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     bio = models.CharField(max_length=500)
#     profile_image = models.ImageField(upload_to="pis/" , blank=True , null=True) 
    
    
#     def __str__(self):
#         return self.name   



class userinfo(models.Model):
    username = models.OneToOneField(User , on_delete=models.CASCADE , primary_key=True) 
    profile_image = models.ImageField(upload_to='pics/' , null=True)
    job = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100 , null=True)
    bio = models.CharField(max_length=100 , null=True , blank=True)
    
    
    



    
    
