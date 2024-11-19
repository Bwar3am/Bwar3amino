from django import forms
from .models import userinfo

class userprofile(forms.ModelForm):
    class Meta:
        model = userinfo
        fields  = ('job' , 'country' , 'city' , 'bio' , 'profile_image')
        
        
class updateprofile(forms.ModelForm):
    class Meta:
        model = userinfo
        fields  = ('job' , 'country' , 'city' , 'bio' , 'profile_image')       
        