from django.contrib import messages
from django.shortcuts import redirect, render
from .models import User, Message, Comment
import bcrypt

# Create your views here.
def index(request):
    if 'user_id' in request.session:
        return redirect('/wall')
    
    return render(request, 'index.html')

def wall(request):
    if 'user_id' not in request.session:
        messages.error(request, "You are not logged in, Please!, Login.")
        return redirect('/')

    context = {
        # 'users': User.objects.all(),
        'all_messages': Message.objects.all().order_by('-created_at'),
        # 'comments': Comment.objects.all().order_by('created_at'),
    }
    return render(request, 'wall.html', context)

def login(request):

    if 'user_id' in request.session:
        return redirect('/wall')
    
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

    return redirect('/wall')

def register(request):

    if 'user_id' in request.session:
        return redirect('/wall')

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

    return redirect('/wall')

def message(request):
    if 'user_id' not in request.session:
        messages.error(request, "You are not logged in, Please!, Login.")
        return redirect('/')

    errors = Message.objects.basic_validator(request.POST)
    if errors:
        for key, val in errors.items():
            messages.error(request, val)

        return redirect('/wall')

    Message.objects.create(
        message=request.POST['message'],
        user=User.objects.get(id=request.session['user_id'])
    )

    messages.success(request, "Message posted successfully!")
    
    return redirect('/wall')

def comment(request):
    if 'user_id' not in request.session:
        messages.error(request, "You are not logged in, Please!, Login.")
        return redirect('/wall')

    errors = Comment.objects.basic_validator(request.POST)
    if errors:
        for key, val in errors.items():
            messages.error(request, val)

        return redirect('/wall')

    Comment.objects.create(
        comment=request.POST['comment'],
        user=User.objects.get(id=request.session['user_id']),
        message=Message.objects.get(id=request.POST['message_id'])
    )

    messages.success(request, "Comment posted successfully!")

    return redirect('/wall')

def logout(request):
    request.session.flush()
    messages.success(request, "You have been logged out successfully.")
    return redirect('/')
