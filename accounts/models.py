from django.db import models
from django.contrib.auth.models import User





class userinfo(models.Model):
    username = models.OneToOneField(User , on_delete=models.CASCADE , primary_key=True) 
    profile_image = models.ImageField(upload_to='pics/' , null=True)
    job = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100 , null=True)
    bio = models.CharField(max_length=100 , null=True , blank=True)
    
    
    



    
    
