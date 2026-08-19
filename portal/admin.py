from django.contrib import admin
from .models import Course , Major , StudentProfile

class CourseAdmin(admin.ModelAdmin):
    list_display = ("code" , "name" , "credits" , "capacity")
    search_fields = ("code" , "name")

admin.site.register(Course , CourseAdmin)
admin.site.register(Major)
admin.site.register(StudentProfile)