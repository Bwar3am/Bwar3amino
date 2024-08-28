from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView 
from django.contrib.auth.views import LogoutView
from .forms import UserProfileForm



class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    
    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')    
    


def profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserProfileForm()
    return render(request, 'profile.html', {'form': form})   


def succses(request):
    return render(request , "success.html")
