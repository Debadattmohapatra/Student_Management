from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from student.models import Student
from student.serializers import StudentSerializer
from django.http.response import JsonResponse
from django.http.response import Http404
# Create your views here.

class StudentView(APIView):
    def get_student(self, pk):
        try:
            student = Student.objects.get(pk=pk)
            return student
        except:
            return JsonResponse("Student Does Not Exist", safe=False)
        
    def get(self, request,pk=None):
        if pk :
            data = self.get_student(pk)
            serializer = StudentSerializer(data)
        else:
            data = Student.objects.all()
            serializer = StudentSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data=request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Student Created Successfully", safe=False)
        return JsonResponse("Failed to Add Student", safe=False)
    
    
    def put(self,request,pk=None):
        student_update=Student.objects.get(pk=pk)
        serializer = StudentSerializer(instance=student_update, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Student Updated Successfully", safe=False)
        return JsonResponse("Failed to Update Student")
    
    def delete(self,request,pk=None):
        student_delete=Student.objects.get(pk=pk)
        student_delete.delete()
        return JsonResponse("Student Deleted Successfully", safe=False)