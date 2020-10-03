from django.shortcuts import render,redirect
from .models import Book2


def index(request):
    books = Book2.objects.all()
    return render(request, 'book/books.html', {'books': books})


def deleteBook(request,id):
    Book2.objects.filter(pk=id).delete()
    return redirect('/book')


def updateBook(request,id):
    book = Book2.objects.filter(id=id)
    if request.method == 'POST':
        book = Book2.objects.get(pk=id)
        book.book_Name = request.POST['book_Name']
        book.author_Name = request.POST['author_Name']
        if request.POST['pub_date']:
            book.pub_date = request.POST['pub_date']
        book.price = request.POST['price']
        if request.FILES:
            book.image = request.FILES['image']
        book.save()
        return redirect('/book')
    else:
        return render(request, 'book/update.html', {'book': book})