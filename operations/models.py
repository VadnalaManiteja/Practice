from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=[('employee', 'Employee'), ('student', 'Student'),('staff', 'Staff')])

    def _str_(self):
        return f"{self.user.username} - {self.role}"

class Contact(models.Model):
    username = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.CharField(max_length=50,null=True,blank=True)
    city = models.CharField(max_length=15,null=True,blank=True)
    pancard = models.CharField(max_length=20,null=True,blank=True)
    state = models.CharField(max_length=15,null=True,blank=True)
    serial_number = models.PositiveIntegerField(default=0)
    profile_picture = models.ImageField(upload_to='contact_pictures/', blank=True, null=True)  # Add this line

    def __str__(self):
         return f"{self.username} - {self.mobile} - {self.city}"

    

class Student(models.Model):
    studentname = models.CharField(max_length=100)
    mothername = models.CharField(max_length=15)
    fathername = models.CharField(max_length=100)
    classA = models.CharField(max_length=15)
    email = models.CharField(max_length=50, null=True, blank=True)
    marks = models.CharField(max_length=15)
    serial_number = models.PositiveIntegerField(default=0)  # New field for display order
    profile_picture = models.ImageField(upload_to='student_pictures/', null=True, blank=True)  # Add this line

    def __str__(self):
        return self.studentname

class Employee(models.Model):
    employeeid=models.CharField(max_length=100)
    employeename=models.CharField(max_length=50)
    email = models.CharField(max_length=50, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    experience = models.CharField(max_length=50, null=True, blank=True,)
    skills=models.CharField(max_length=50,null=True, blank=True,)
    salary = models.CharField(max_length=50, null=True, blank=True)
    serial_number = models.PositiveIntegerField(default=0)
    profile_picture = models.ImageField(upload_to='employee_pictures/', blank=True, null=True)  # Add this line

    def __str__(self):
        return self.employeename
    

class Task(models.Model):
    Taskname = models.CharField(max_length=100)
    Startingdate = models.CharField(max_length=15)
    Endingdate = models.CharField(max_length=100)
    Status = models.CharField(max_length=15,null=True,blank=True)
    serial_number = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.Taskname




