from django.shortcuts import render
from .models import  Teacher
from .forms import  Register

def index(request):
    teachers = Teacher.objects.all()
    return render(request,'teacher/index.html', {'teachers': teachers})


def register(request):
    register = Register()
    return render(request,'teacher/register.html',{'register': register})