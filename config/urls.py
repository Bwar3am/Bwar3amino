from django.contrib import admin
from django.urls import path ,  include
from  config import views
from config.views import *
from .forms import *


urlpatterns = [
    path("" , views.home , name='home' ),
    path("about/" , views.about , name="about"),
    path("content/<str:pk>" , views.content , name = "content"),
    path("register" , views.register , name = "register"),
    # path("test" , views.CommentFormView.as_view() , name="test")
   

    
]
