from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Teacher
from .forms import Register,Login

def index(request):
    teachers = Teacher.objects.all()
    return render(request,'teacher/index.html', {'teachers': teachers})


def register(request):
    if request.method =='POST':
        teacher  = Teacher()
        form = Register(request.POST)
        if form.is_valid():
            teacher = form.save(commit=False)
            form.save()
            return HttpResponse('You are Registered')
        else:
            return HttpResponse("You are not Registered")
    else:
        register = Register()
        return render(request,'teacher/register.html',{'register': register})


def login(request):
    if request.method=='POST':
        name = request.POST['name']
        password = request.POST['password']
        teacher = Teacher.objects.filter(name=name, password=password).first()
        if teacher:
            request.session['name'] = name
            return redirect('/teacher')
        else:
            return redirect('/teacher/login')
    else:
        login = Login()
        return render(request,'teacher/login.html',{'login':login})


def logout(request):
    request.session.flush()
    return  redirect('/teacher')