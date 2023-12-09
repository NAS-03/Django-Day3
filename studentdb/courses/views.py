from django.shortcuts import render
from courses.models import Courses
# Create your views here.

def CourseView(request):
    courses = Courses.objects.all()

    return render(request,'course.html',{'courses':courses})