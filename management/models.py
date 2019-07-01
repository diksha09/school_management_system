from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

DEPARTMENT_NAME = (
    ('CS', 'computer science'),
    ('M', 'mathematics'),
    ('ENG', 'english'),
    ('HND', 'hindi'),
    ('SCI', 'science')
    )

GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )


class SchoolUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    dob = models.DateField(blank=True, null=True)
    role = models.IntegerField()
    profile_pic = models.CharField(max_length=255, default="")
    gender = models.CharField(max_length=1, default="m")
    user_auth = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, default="")
    firstname = models.CharField(max_length=60, blank=True, null=True)
    lastname = models.CharField(max_length=60, blank=True, null=True)
    phone_no = models.CharField(null=True, max_length=12)
    status = models.IntegerField(default=1)
    
    class Meta:
        db_table = 'user_info'

    
class Klass(models.Model):
    grade = models.IntegerField(blank=False)
    total_student = models.IntegerField(null=True, default=0)
    
    class Meta:
        db_table = "klass_info"


class Div(models.Model):
    d_id = models.BigAutoField(primary_key=True)
    klass = models.ForeignKey(Klass, blank=True, on_delete=models.CASCADE)
    division = models.CharField(max_length=50, blank=True, null=True)
    
    class Meta:
        db_table = "class_div"


class Student(models.Model):
    s_id = models.ForeignKey(SchoolUser, blank=True, on_delete=models.CASCADE) 
    klass = models.ForeignKey(Klass, blank=True, on_delete=models.CASCADE)
    div = models.ForeignKey(Div, blank=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "student_info"
        

class StudAtt(models.Model):
    s_id = models.ForeignKey(SchoolUser, blank=True, on_delete=models.CASCADE)
    a_date = models.DateField(blank=True, null=True)
    a_status = models.CharField(max_length=10, blank=True, null=True)
    klass = models.ForeignKey(Klass, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "student_att"
    
    
class StudentFee(models.Model):
    s_id = models.ForeignKey(SchoolUser, blank=True, on_delete=models.CASCADE)
    total_amount = models.IntegerField()

    class Meta:
        db_table = 'fees'


class Subject(models.Model):
    sub_id = models.BigAutoField(primary_key=True)
    sub_name = models.CharField(max_length=100)
    marks = models.IntegerField(null=True)
    pass_marks = models.IntegerField(null=True)
    s_id = models.ForeignKey(SchoolUser, blank=True, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "subject_info"

    
class Teacher(models.Model):
    s_id = models.ForeignKey(SchoolUser, blank=True, on_delete=models.CASCADE)
    designation = models.CharField(null=False, max_length=30)
    joined = models.DateField('Year-Month')
       
    class Meta:
        db_table = 'teacher'


class Department(models.Model):
    s_id = models.ForeignKey(SchoolUser, blank=True, on_delete=models.CASCADE)
    dept_id = models.IntegerField(primary_key=True)
    dept_name = models.CharField(max_length=10, choices=DEPARTMENT_NAME)
    dept_head = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        db_table = 'department'


class TeachAtt(models.Model):
    s_id = models.ForeignKey(SchoolUser, blank=True, on_delete=models.CASCADE)
    a_date = models.DateField(blank=True, null=True)
    a_status = models.CharField(max_length=10, blank=True, null=True)
    
    class Meta:
        db_table = "teacher_att"


class AssiTeacher(models.Model):
    klass = models.ForeignKey(Klass, blank=True, on_delete=models.CASCADE)
    div = models.ForeignKey(Div, blank=True, on_delete=models.CASCADE)
    s_id = models.ForeignKey(SchoolUser, blank=True, null=True, default="", on_delete=models.CASCADE)
    
    class Meta:
        db_table = "Assign_teacher"

# Create your models here.
