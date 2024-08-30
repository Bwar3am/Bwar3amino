from django.shortcuts import render , get_object_or_404
from django.core.paginator import Paginator
from .models import *
from django.shortcuts import redirect
from accounts.models import userinfo
# Create your views here.


def home(request):
    
    info = blog.objects.all()
    pagechanger = Paginator(info , 4)
    page_number = request.GET.get("page")
    page_obj = pagechanger.get_page(page_number)
    context = {"info":info , "page_obj":page_obj }
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
    paginator = Paginator(info, 6)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    
    info.view_count += 1
    info.save()
    context = {"info":info , "content":content}
    return render(request ,"content.html" , context )


def register(request):
    return render(request , "register.html")


# def profile_view(request):
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('profile_success')
#     else:
#         form = UserProfileForm()
#     return render(request, 'profile.html', {'form': form})


# def succses(request):
#     return render(request , )