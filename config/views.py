from django.shortcuts import render

from .models import *

# Create your views here.


def home(request):
    return render(request , "index1.html")


def about(request):
    return render (request , "aboutme.html")
