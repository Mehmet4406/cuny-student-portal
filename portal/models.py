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

    def __str__(self):
        return f"{self.code} - {self.name}"

class StudentProfile (models.Model):
    user = models.OneToOneField(User , on_delete = models.CASCADE)
    student_id = models.CharField(max_length = 10 , unique = True)
    major = models.ForeignKey(Major , on_delete = models.SET_NULL , null = True , blank = True)

    def __str__(self):
        return f"{self.student_id} - {self.user.get_full_name()}"

class Semester(models.Model):
    name = models.CharField(max_length = 50 , unique = True)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default = False)

    def __str__(self):
        return self.name


class AcademicDepartment(models.Model):
    name = models.CharField(max_length = 100 , unique = True)

    def __str__(self):
        return self.name
    
class ProfessorProfile(models.Model):
    user = models.OneToOneField(User , on_delete = models.CASCADE)
    professor_id = models.CharField(max_length = 10 , unique = True ,editable = False)
    academic_department = models.ForeignKey(AcademicDepartment , on_delete= models.PROTECT)

    def save(self , *args , **kwargs):
        if not self.professor_id:
            existing_ids = ProfessorProfile.objects.values_list("professor_id" , flat = True)
            numeric_ids = [int(professor_id[1:]) for professor_id in existing_ids if professor_id.startswith("P") and professor_id[1:].isdigit()]
            next_id = max(numeric_ids , default = 0) + 1

            self.professor_id = f"P{next_id:03d}"
        super().save(*args , **kwargs) 

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.professor_id}"

class Enrollment(models.Model):
    student = models.ForeignKey(StudentProfile , on_delete = models.CASCADE)
    course = models.ForeignKey(Course , on_delete = models.CASCADE)
    semester = models.ForeignKey(Semester , on_delete = models.CASCADE)
    grade = models.CharField(max_length = 2 , blank = True)
    enrolled_at = models.DateField(auto_now_add = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
            fields = ["student" , "course" , "semester"] ,
            name = "unique_student_course_semester"
        )
        ] 

    def __str__(self):
        return f"{self.student.student_id} - {self.course.code} - {self.semester.name}"

class Section(models.Model):

    INSTRUCTION_MODE_CHOICES = [
        ("REGULAR" , "Regular") ,
        ("ONLINE_MEETING" , "Online Meeting") ,
        ("ONLINE_SYNCHRONIZE" , "Online Synchronize") ,
    ]

    course = models.ForeignKey(Course , on_delete = models.CASCADE)
    subcode = models.CharField(max_length = 10 , editable = False)
    professor = models.CharField(max_length = 100)
    days = models.CharField(max_length = 10)
    start_time = models.TimeField(null = True , blank = True)
    end_time = models.TimeField(null = True , blank = True)
    capacity = models.PositiveIntegerField(default = 30)
    instruction_mode = models.CharField(max_length = 50 , choices = INSTRUCTION_MODE_CHOICES)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ["course" , "subcode"] ,
                name = "unique_course_subcode"
            )
        ]

    def save(self , *args , **kwargs):
        # Only generate a subcode if this Section does not already have one.
        # This prevents the subcode from changing when we edit an existing Section.
        if not self.subcode:

            # Get the subcodes of all existing Sections that belong
            # to the SAME Course.
            # Example:
            # CSC101 may already have:
            # 4401, 4402, 4403
            existing_subcodes = Section.objects.filter(course = self.course).values_list("subcode" , flat = True)

            # Convert numeric subcodes from strings into integers.
            # Example:
            # ["4401", "4402"] → [4401, 4402]
            # isdigit() protects us in case a non-numeric value
            # somehow exists in the database.
            numeric_subcodes = [int(code) for code in existing_subcodes if code.isdigit()]

            # Find the highest existing subcode and add 1.
            # If this Course has no Sections yet:
            # default = 4400
            # 4400 + 1 = 4401
            # If CSC101 already has 4401 and 4402:
            # max = 4402
            # 4402 + 1 = 4403
            next_subcode = max(numeric_subcodes , default = 4400) + 1

            # subcode is a CharField, so convert the number
            # back into a string before storing it.
            self.subcode = str(next_subcode)

        # Run Django's normal save() method.
        # This is the step that actually saves the Section
        # into the database
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.course.code} - {self.subcode} - {self.course.name}"

