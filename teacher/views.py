from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import Teacher
from .forms import Register,Login


def index(request):
    teachers = Teacher.objects.all()
    return render(request,'teacher/index.html', {'teachers': teachers})


def register(request):
    if request.method =='POST':
        teacher = Teacher()
        form = Register(request.POST, request.FILES)
        if form.is_valid():
            teacher = form.save(commit=False)
            form.save()
            return render(request, 'teacher/login.html')
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


def deleteTeacher(request, id):
    teacher = Teacher.objects.filter(id=id)
    teacher.delete()
    return redirect('/teacher')


def updateTeacher(request, id):
    if request.method == 'GET':
        teacher = Teacher.objects.filter(id=id)
        return render(request,'teacher/update.html', {'teacher': teacher})
    else:
        teacher = Teacher.objects.get(pk=id)
        teacher.name = request.POST['name']
        teacher.password = request.POST['password']
        teacher.subject_Name = request.POST['subject_Name']
        teacher.qualification = request.POST['qualification']
        if request.FILES:
            teacher.image = request.FILES['image']
            print(request.FILES)
        teacher.save()
        return  redirect('/teacher')

def logout(request):
    request.session.flush()
    return  redirect('/teacher')