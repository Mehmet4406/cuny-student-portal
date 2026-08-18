from django.db import models

class Course(models.Model):
    code = models.CharField(max_length = 20)
    name = models.CharField(max_length = 200)
    credits = models.IntegerField()

    def __str__(self):
        return f"{self.code} - {self.name}"