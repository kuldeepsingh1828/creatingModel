from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('delete/<int:id>', views.deleteTeacher, name='delete'),
    path('update/<int:id>', views.updateTeacher, name='update'),
    ]
