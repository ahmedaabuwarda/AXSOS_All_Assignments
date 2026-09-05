from django.contrib import messages

import bcrypt
from django.shortcuts import redirect, render
from .models import User

# Create your views here.
def index(request):
    if 'user_id' in request.session:
        return redirect('/success')
    
    return render(request, 'index.html')

def login(request):

    if 'user_id' in request.session:
        return redirect('/success')
    
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

    return redirect('/success')

def register(request):

    if 'user_id' in request.session:
        return redirect('/success')

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
    
    return redirect('/success')

def success(request):
    if 'user_id' in request.session:
        return render(request, 'success.html')
    

    messages.error(request, "You are not logged in, Please!, Login.")
    return redirect('/')

def logout(request):
    # Clear the session or any authentication tokens here
    request.session.flush()  # This will clear all session data
    messages.success(request, "You have been logged out.")
    
    return redirect('/')
