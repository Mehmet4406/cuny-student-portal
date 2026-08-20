from django.contrib import admin
from .models import Course , Major , StudentProfile , Semester , Enrollment , Section , AcademicDepartment , ProfessorProfile
from .forms import ProfessorAdminForm 
from django.contrib.auth.models import User

class CourseAdmin(admin.ModelAdmin):
    list_display = ("code" , "name" , "credits")
    search_fields = ("code" , "name")

class ProfessorProfileAdmin(admin.ModelAdmin):
    form = ProfessorAdminForm

    list_display = ("professor_id" , "professor_name" , "professor_email" , "academic_department")
    search_fields = ("professor_id" , "user__first_name" , "user__last_name" , "user__email" , "user__username")
    list_filter = ("academic_department" , )

    def professor_name(self , obj):
        return obj.user.get_full_name()

    def professor_email(self , obj):
        return obj.user.email

    def save_model(self, request, obj, form, change):

        if not change:
            user = User.objects.create_user(
                username = form.cleaned_data["username"] ,
                email = form.cleaned_data["email"] ,
                password = form.cleaned_data["password1"] ,
                first_name = form.cleaned_data["first_name"] ,
                last_name = form.cleaned_data["last_name"] ,
            )
            obj.user = user

        else:
            user = obj.user
            user.first_name = form.cleaned_data["first_name"] 
            user.last_name = form.cleaned_data["last_name"] 
            user.email = form.cleaned_data["email"] 
            user.username = form.cleaned_data["username"] 

            new_password = form.cleaned_data.get("password1")

            if new_password:
                user.set_password(new_password)

            user.save()

            

        super().save_model(request, obj, form, change)

admin.site.register(Course , CourseAdmin)
admin.site.register(Major)
admin.site.register(StudentProfile)
admin.site.register(Semester)
admin.site.register(Enrollment)
admin.site.register(Section)
admin.site.register(AcademicDepartment)
admin.site.register(ProfessorProfile , ProfessorProfileAdmin)