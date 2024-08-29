from django import forms
from .models import userinfo


# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = users
#         fields = ['name', 'last_name' ,'profile_image', 'bio']


class userprofile(forms.ModelForm):
    class Meta:
        model = userinfo
        fields  = [     'job' , 'country' , 'city' , 'bio']
        