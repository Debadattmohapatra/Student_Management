from django.db import models

# Create your models here.
class Student(models.Model):
    StudentId=models.AutoField(primary_key=True)
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    RegistrationNo=models.CharField(max_length=100)
    Email=models.EmailField(max_length=200)
    Course=models.CharField(max_length=200)