from rest_framework import serializers
from student.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('StudentId','FirstName','LastName','RegistrationNo','Email','Course')