from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class userinfo(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE , primary_key=True) 
    profile_image = models.ImageField(upload_to='pics/' , null=True , default="pics/placeholder.jpg")
    job = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100 , null=True)
    bio = models.CharField(max_length=100 , null=True , blank=True)

    def __str__(self):
        return self.user.username
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        userinfo.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userinfo.save()



    



    
    

