from django.contrib import admin
from student.models import Student
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['StudentId','FirstName','LastName','RegistrationNo','Email','Course']