from django.db import models

# Create your models here.


class users(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.CharField(max_length=500)
    profile_image = models.ImageField(upload_to="pis/" , blank=True , null=True) 
    
    
    def __str__(self):
        return self.name   
    
    
