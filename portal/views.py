from django.http import HttpResponse 
from django.shortcuts import render
from .models import Course

def home(request):
    return render(request , "portal/home.html")

def courses(request):

    course_list = Course.objects.all()

    return render(request , "portal/courses.html" , {"course_list" : course_list })