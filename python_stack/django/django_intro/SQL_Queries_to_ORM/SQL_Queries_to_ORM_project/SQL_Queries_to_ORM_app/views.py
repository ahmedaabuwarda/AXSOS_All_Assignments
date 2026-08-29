import datetime

from django.shortcuts import render, redirect
from .models import users

# Create your views here.
def index(request):

    context = {
        "all_the_users": users.objects.all()
    }

    # print(context)
    
    return render(request,'index.html', context)

def create(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email_Address = request.POST['email_address']
    age = request.POST['age']

    time = datetime.datetime.now()
    print(time)

    users.objects.create(first_name=first_name, last_name=last_name, email_address=email_Address, age=age, created_at="2026-08-01", updated_at="2026-08-01")
    return redirect('/')

