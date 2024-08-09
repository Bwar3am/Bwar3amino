from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class blog(models.Model):
    title = models.CharField(max_length=100 , null=True)
    time_created = models.TimeField(auto_now=True , null=False)
    description = models.CharField(max_length=250 ,null=True)
    # author = models.ForeignKey(User ,on_delete=models.CASCADE , null=False)
    body = models.CharField(max_length=10000 , null=False)
    
