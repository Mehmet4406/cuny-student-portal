from django.contrib import admin
from .models import Course , Major , StudentProfile , Semester , Enrollment , Section , AcademicDepartment

class CourseAdmin(admin.ModelAdmin):
    list_display = ("code" , "name" , "credits")
    search_fields = ("code" , "name")

admin.site.register(Course , CourseAdmin)
admin.site.register(Major)
admin.site.register(StudentProfile)
admin.site.register(Semester)
admin.site.register(Enrollment)
admin.site.register(Section)
admin.site.register(AcademicDepartment)