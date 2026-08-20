from django.http import HttpResponse 
from django.shortcuts import render , redirect , get_object_or_404
from .models import Course , StudentProfile , Semester
from .forms import StudentSignUpForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request , "portal/home.html")


@login_required
def dashboard(request):

        student = request.user.studentprofile
        return render(request , "portal/dashboard.html" , {"student" : student})


@login_required
def student_profile(request):

    student = request.user.studentprofile
    return render(request , "portal/student_profile.html" , {"student" : student})

@login_required
def select_semester(request):
    semesters = Semester.objects.all()
    return render(request , "portal/select_semester.html" , {"semesters" : semesters})

@login_required
def select_courses(request, semester_name):
    semester = get_object_or_404(Semester , name = semester_name)
    courses = Course.objects.all()
    return render(request , "portal/select_courses.html" , {"semester" : semester , "courses" : courses})


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
