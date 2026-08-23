from django.shortcuts import render

# Create your views here.
def users(request):
    return render(request, 'users.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')