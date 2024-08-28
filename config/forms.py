from django import forms
from .models import users

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = users
        fields = ['profile_picture', 'bio']
        
    
