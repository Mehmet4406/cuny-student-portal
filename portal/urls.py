from django.urls import path              #"" is the app's main adress#
from . import views                       #views.home runs the home function inside views.py()#
                                          #name = home names the URL inside the django#


urlpatterns = [
    path("" , views.home , name = "home"),  
    path("courses/" , views.courses , name = "courses"),

    ]     