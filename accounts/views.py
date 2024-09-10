from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView 
from django.contrib.auth.views import LogoutView
from django.views.generic.edit import UpdateView
from .forms import userprofile , updateprofile
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from .models import *



class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    
    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home') 
    
    
    
def displayprofile(request):
    return render(request , "displayprofile.html")


class CustomPasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_change_done')
    template_name = "registration/change_password.html"



class updateprofile(UpdateView):
    model = userinfo
    form_class = updateprofile
    template_name = 'updateprofile.html'
    success_url = reverse_lazy('displaying')
    
    

 
    
    
    


def profile_view(request):
    if request.method == 'POST':
        form = userprofile(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = userprofile()
    return render(request, 'profile.html', {'form': form})   


def succses(request):
     return render(request , "success.html")
 
 
# def profiledispaly(request , pk):
#     profile = userinfo.objects.get(pk=id)
#     context = {"profile" : profile}
    
#     return render (request , "index1.html" , context)
     
 
 
 
      
 
 
