from django.shortcuts import render
from .models import Book2


def index(request):
    books = Book2.objects.all()
    return  render(request, 'book/books.html', {'books': books})