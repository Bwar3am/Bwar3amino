from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from .views import SignUpView
from .views import CustomLogoutView
from django.contrib.auth.views import PasswordChangeDoneView
from .views import *

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/" , views.profile_view , name="profile" ),
    # path("logout/", auth_views.LogoutView.as_view(template_name='registration/logged_out.html',next_page=None), name="logout")
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('succsess' , views.succses , name="success"),
    path("dispaly" , views.displayprofile , name="displaying"),
    path("updateprofile/<int:pk>/edit" , updateprofile.as_view() , name="updateprofile"),
    path('password/', CustomPasswordChangeView.as_view(), name='change_password'),
    path('password/done/', PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done')
]