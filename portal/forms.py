from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ProfessorProfile

# Custom sign-up form for student users.
# It extends Django's built-in UserCreationForm.
class StudentSignUpForm(UserCreationForm):

    # Extra fields that we want to collect during sign-up.
    first_name = forms.CharField(max_length = 100)
    last_name = forms.CharField(max_length = 100)
    email = forms.EmailField()

    # Custom validation method for the email field.
    # Django automatically calls clean_<fieldname>() during form validation.
    def clean_email(self):

        # Get the validated email value from the form data.
        email = self.cleaned_data["email"]

        # Check if a User with the same email already exists.
        # iexact makes the comparison case-insensitive.
        if User.objects.filter(email__iexact = email).exists():
            raise forms.ValidationError("This email is already in use.")    # Stop validation and show this error on the form.

        return email

    # Meta tells Django which model this form is connected to
    # and which fields should be included in the form.
    class Meta:

        # This form will create/update Django User objects
        model = User 
        fields = (          # These are the fields that will appear in the sign-up form.
            "username" , 
            "first_name" ,
            "last_name" ,
            "email" ,
            "password1" ,
            "password2"
        )


class ProfessorAdminForm(forms.ModelForm):
    # These fields belong to Django's User model.
    # We manually add them here because ProfessorProfile itself
    # only stores user, professor_id, and academic_department
    first_name = forms.CharField(max_length = 100)
    last_name = forms.CharField(max_length = 100)
    email = forms.EmailField()
    username = forms.CharField(max_length = 150)

    # PasswordInput hides the password characters on the screen.
    # required=False because when EDITING an existing professor,
    # we do not want to force the admin to change the password.
    password1 = forms.CharField(label = "Temporary Password" , widget = forms.PasswordInput() , required = False)
    password2 = forms.CharField(label = "Confirm Temporary Password" , widget = forms.PasswordInput() , required = False)

    class Meta:
        # This form is mainly connected to ProfessorProfile.
        model = ProfessorProfile

        # These are the fields that will appear in the admin form.
        fields = ("first_name" , "last_name" , "email" , "username" , "password1" , "password2" , "academic_department" , )

    def __init__(self , *args , **kwargs):
        # Run Django's normal ModelForm setup first.
        # Without this, Django would not create self.fields,
        # self.instance, validation data, etc.
        super().__init__(*args , **kwargs)

        # If self.instance has a primary key (pk),
        # we are EDITING an existing ProfessorProfile.
        if self.instance and self.instance.pk:

            # Get the Django User connected to this professor.
            user = self.instance.user

            #Pre-fill the form fields with the current User data#
            self.fields["first_name"].initial = user.first_name
            self.fields["last_name"].initial = user.last_name
            self.fields["email"].initial = user.email
            self.fields["username"].initial = user.username

        # If there is no saved ProfessorProfile yet,
        # we are CREATING a new professor.
        # A password is required for a new account.
        else:
            self.fields["password1"].required = True
            self.fields["password2"].required = True


    def clean_email(self):
        email = self.cleaned_data["email"]
        users = User.objects.filter(email__iexact = email)

        if self.instance and self.instance.pk:
            users = users.exclude(pk = self.instance.user_id)

        if users.exists():
            raise forms.ValidationError("This email is already in use.")

        return email


    def clean_username(self):
        username = self.cleaned_data["username"]
        users = User.objects.filter(username__iexact = username)

        if self.instance and self.instance.pk:
            users = users.exclude(pk = self.instance.user_id)

        if users.exists():
            raise forms.ValidationError("This username is choosen")

        return username

    def clean_password(self):
        cleaned_data = super().clean()
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 or password2:
            if password1 != password2:
                self.add_error("password2" , "Passwords do not match")

        return cleaned_data 