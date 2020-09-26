from django.shortcuts import render


def index(request):
    return render(request, 'first/index.html')


def register(request):
    return render(request,'first/register.html')


def login(request):
    return render(request,'first/login.html')