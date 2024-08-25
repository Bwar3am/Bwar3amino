from django.db import models

# Create your models here.


class profile (models.Model):
    name = models.CharField(max_length=20 , null=False)
    last_name = models.CharField(max_length=20 , null=False)
    email_address = models.EmailField(null=False)
    profile_image = models.ImageField(null=True)
    bio = models.CharField(null=False , max_length=300)
    # about = models.CharField(null=False , max_length=100)
    
    
