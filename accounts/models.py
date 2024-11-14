from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save



class userinfo(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE , primary_key=True) 
    profile_image = models.ImageField(upload_to='pics/' , null=True)
    job = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100 , null=True)
    bio = models.CharField(max_length=100 , null=True , blank=True)

    def __str__(self):
        return self.user.username
    
def create_profile(sender , instance , created , **kwargs):
    if created:
        user_profile = userinfo(user=instance)
        user_profile.save()

post_save.connect(create_profile , sender=User)


    



    
    

