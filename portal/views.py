from django.http import HttpResponse 
from django.shortcuts import render , redirect
from .models import Course , StudentProfile
from .forms import StudentSignUpForm

def home(request):
    return render(request , "portal/home.html")

def courses(request):

    course_list = Course.objects.all()

    return render(request , "portal/courses.html" , {"course_list" : course_list })

def signup(request):
    # GET request:
    # The user is opening the sign-up page, so we show an empty form.
    # POST request:
    # The user submitted the form, so we validate the submitted data.
    if request.method == "POST":

        # Fill the form with the data sent from the browser.
        form = StudentSignUpForm(request.POST)

        # If all form fields pass validation, create the user.
        if form.is_valid():

            # Save the form and create a new Django User in the database.
            user = form.save()

            # Create a StudentProfile linked to the new User.
            StudentProfile.objects.create(user = user, student_id = f"S{user.id:03d}"
            )

            return redirect("home")

    else:
        # No form was submitted, so create an empty sign-up form.
        form = StudentSignUpForm()

    # Show the sign-up page and send the form to the HTML template.
    return render(request, "portal/signup.html", {"form": form}
    )
