from django.shortcuts import render, redirect
from .models import Author, Book

# Create your views here.
def index(request):
    context = {
        "authors": Author.objects.all(),
        "books": Book.objects.all(),
    }
    return render(request, 'index.html', context)

def add_author(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']

    Author.objects.create(first_name=first_name, last_name=last_name)
    return redirect('/')


def add_book(request):
    title = request.POST['title']
    desc = request.POST['desc']
    
    Book.objects.create(title=title, desc=desc)
    return redirect('/')

def add_author_to_book(request):
    book_id = request.POST['book_id']
    author_id = request.POST['author_id']
    author = Author.objects.get(id=author_id)
    book = Book.objects.get(id=book_id)
    book.authors.add(author)

    return redirect('/')

def add_book_to_author(request):
    book_id = request.POST['book_id']
    author_id = request.POST['author_id']
    author = Author.objects.get(id=author_id)
    book = Book.objects.get(id=book_id)
    author.books.add(book)

    return redirect('/')


def show_book(request, book_id):

    book = Book.objects.get(id=book_id)
    authors = Author.objects.all()

    context = {
        "book": book,
        "book_authors": book.authors.all(),
        "authors": authors,
    }

    return render(request,'show_book.html',context)


def show_author(request, author_id):

    author = Author.objects.get(id=author_id)
    books = Book.objects.all()

    context = {
        "author": author,
        "author_books": author.books.all(),
        "books": books,
    }

    return render(request,'show_author.html',context)
