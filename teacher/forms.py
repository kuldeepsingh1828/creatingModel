from django import forms
from .models import Teacher


class Register(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name','subject_Name','qualification','image']
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control mt-2'}),
            "subject_Name": forms.TextInput(attrs={'class': 'form-control mt-2'}),
            "qualification": forms.TextInput(attrs={'class': 'form-control mt-2'}),
            "image": forms.FileInput(attrs={'class': 'form-control mt-2'}),
        }


class Login(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name','password']
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control mt-2'}),
            "password" : forms.PasswordInput(attrs={'class': 'form-control mt-2'}),
        }