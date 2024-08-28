from django import forms
from .models import users


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = users
        fields = ['name', 'last_name' ,'profile_image', 'bio']
        