from django.shortcuts import render

from .models import *

# Create your views here.


def home(request):
    info = blog.objects.all()
    context = {"info":info}
    return render(request , "index1.html" , context)


def about(request):
    return render (request , "aboutme.html")
