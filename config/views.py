from django.shortcuts import render

from .models import *

# Create your views here.


def home(request):
    info = blog.objects.all()
    context = {"info":info}
    return render(request , "index1.html" , context)


def about(request):
    return render (request , "aboutme.html")

def author(request):
    info = author.objects.all()
    context = {"info" : info}
    return render(request, "index1.html" , context)


def content(request , pk ):
    info = blog.objects.get(id=pk)
    content = blog.objects.get(id=pk)
    context = {"info":info , "content":content}
    return render(request ,"content.html" , context )