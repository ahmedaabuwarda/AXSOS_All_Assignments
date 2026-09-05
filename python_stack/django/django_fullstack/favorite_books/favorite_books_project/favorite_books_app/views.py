from django.shortcuts import redirect, render
from django.contrib import messages
from .models import User, Book
import bcrypt

# Create your views here.
def index(request):
    if 'user_id' in request.session:
        return redirect('/books')
    
    return render(request, 'index.html')

# authentication views
def login(request):

    if 'user_id' in request.session:
        return redirect('/')
    
    errors = User.objects.login_validator(request.POST)

    if errors:
        for key,val in errors.items():
            messages.error(request, val)

        return redirect('/')

    # if not errors, you can proceed with login logic here
    user = User.objects.filter(email=request.POST['email']).first()

    if not user:
        messages.error(request, "Invalid email or password")
        return redirect('/')

    if not bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        messages.error(request, "Invalid email or password")
        return redirect('/')

    messages.success(request, "Login successful!")

    # add user id to session
    request.session['user_id'] = user.id
    request.session['first_name'] = user.first_name  # Store first name in session for personalized greeting

    return redirect('/books')

def register(request):

    if 'user_id' in request.session:
        return redirect('/')

    errors = User.objects.register_validator(request.POST)

    if errors:
        for key,val in errors.items():
            messages.error(request, val)

        return redirect('/')

    # if not errors, you can proceed with registration logic here
    user = User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password=bcrypt.hashpw(
            request.POST['password'].encode(),
            bcrypt.gensalt()
        ).decode()
    )

    messages.success(request, "Registration successful! Please log in.")

    # add user id to session
    request.session['user_id'] = user.id
    request.session['first_name'] = user.first_name  # Store first name in session for personalized greeting

    return redirect('/books')

def logout(request):
    request.session.flush()  # Clear the session data
    messages.success(request, "You have been logged out successfully.")
    return redirect('/')  # Redirect to the index page after logout

def books(request):
    if 'user_id' not in request.session:
        messages.error(request, "You are not logged in, Please!, Login.")
        return redirect('/')

    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'books': Book.objects.all(),
    }
    return render(request, 'books.html', context)

def show(request, book_id):
    if 'user_id' not in request.session:
        messages.error(request, "You are not logged in, Please!, Login.")
        return redirect('/')

    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'book': Book.objects.get(id=book_id),
    }
    return render(request, 'show.html', context)

def store(request):
    if 'user_id' not in request.session:
        messages.error(request, "You are not logged in, Please!, Login.")
        return redirect('/')

    print(request.POST)

    errors = Book.objects.basic_validator(request.POST)
    if errors:
        for key, val in errors.items():
            messages.error(request, val)

        return redirect('/books')

    # Create the book and associate it with the logged-in user + favorite it
    book = Book.objects.create(
        title=request.POST['title'],
        description=request.POST['description'],
        uploaded_by=User.objects.get(id=request.session['user_id'])
    )
    book.users_who_favorited.add(book.uploaded_by)
    messages.success(request, "Book added successfully!")
    return redirect('/books')

def update(request, book_id):
    if 'user_id' not in request.session:
        messages.error(request, "You are not logged in, Please!, Login.")
        return redirect('/')

    book = Book.objects.get(id=book_id)

    # Check if the logged-in user is the one who uploaded the book
    if book.uploaded_by.id != request.session['user_id']:
        messages.error(request, "You are not authorized to update this book.")
        return redirect('/books')

    errors = Book.objects.basic_validator(request.POST)
    if errors:
        for key, val in errors.items():
            messages.error(request, val)

        return redirect(f'/books/{book_id}')

    # Update the book details
    book.title = request.POST['title']
    book.description = request.POST['description']
    book.save()

    messages.success(request, "Book updated successfully!")

    return redirect(f'/books/{book_id}')

def add_favorite(request, book_id):
    if 'user_id' not in request.session:
        messages.error(request, "You are not logged in, Please!, Login.")
        return redirect('/')

    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=request.session['user_id'])

    if not book.users_who_favorited.filter(id=user.id).exists():
        book.users_who_favorited.add(user)
        messages.success(request, "Book added to favorites!")
    else:
        messages.info(request, "This book is already in your favorites.")

    return redirect('/books')

def remove_favorite(request, book_id):
    if 'user_id' not in request.session:
        messages.error(request, "You are not logged in, Please!, Login.")
        return redirect('/')

    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=request.session['user_id'])

    # Remove the book from the user's favorites
    book.users_who_favorited.remove(user)

    messages.success(request, "Book removed from favorites!")
    return redirect('/books')