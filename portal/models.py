from django.db import models
from django.contrib.auth.models import User


class Major(models.Model):
    name = models.CharField(max_length = 100 , unique = True)

    def __str__(self):
        return self.name

class Course(models.Model):
    code = models.CharField(max_length = 20)
    name = models.CharField(max_length = 200)
    credits = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField(default = 30 )

    def __str__(self):
        return f"{self.code} - {self.name}"

class StudentProfile (models.Model):
    user = models.OneToOneField(User , on_delete = models.CASCADE)
    student_id = models.CharField(max_length = 10 , unique = True)
    major = models.ForeignKey(Major , on_delete = models.SET_NULL , null = True , blank = True)

    def __str__(self):
        return f"{self.student_id} - {self.user.get_full_name()}"
    