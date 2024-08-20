from django.shortcuts import render , get_object_or_404

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
    # counting = get_object_or_404(blog , id=pk )
    info.view_count = info.view_count + 1
    info.save()
    context = {"info":info , "content":content } 
    return render(request ,"content.html" , context )


def register(request):
    return render(request , "register.html")