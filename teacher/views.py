from django.shortcuts import render
from .models import  Teacher

def index(request):
    teachers = Teacher.objects.all()
    return render(request,'teacher/index.html', {'teachers': teachers})