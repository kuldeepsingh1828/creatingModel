from . import views

from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:id>', views.updateBook, name='update'),
    path('delete/<int:id>', views.deleteBook, name='update'),
]