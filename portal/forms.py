from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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