from django.urls import path              
from . import views                     
from django.contrib.auth import views as auth_views 


urlpatterns = [
    path("" , views.home , name = "home") ,  
    path("courses/" , views.courses , name = "courses") ,
    path("signup/" , views.signup , name = "signup") ,
    path("login/" , auth_views.LoginView.as_view(template_name = "portal/login.html", redirect_authenticated_user = True) , name = "login") ,
    path("logout/" , auth_views.LogoutView.as_view() , name = "logout") , 
    ]     