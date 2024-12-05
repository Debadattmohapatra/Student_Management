from django.urls import path
from student import views

urlpatterns = [
    path('students/',views.StudentView.as_view()),
    path('students/<int:pk>/',views.StudentView.as_view()),
    
]
