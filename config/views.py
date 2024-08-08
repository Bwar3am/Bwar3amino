from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request , "index1.html")


def about(request):
    return render (request , "aboutme.html")
