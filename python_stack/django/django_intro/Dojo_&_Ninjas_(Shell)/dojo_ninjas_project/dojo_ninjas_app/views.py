from django.shortcuts import render, redirect
from .models import Dojo, Ninja

# Create your views here.
def index(request):
    context = {
        "dojos" : Dojo.objects.all()
    }
    return render(request,'index.html', context)\

def dojo(request):
    name = request.POST['name']
    city = request.POST['city']
    state = request.POST['state']

    Dojo.objects.create(name=name, city=city, state=state)

    return redirect('/')


def ninja(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    dojo_id = request.POST['dojo_id']

    Ninja.objects.create(first_name=first_name, last_name=last_name, dojo=Dojo.objects.get(id=dojo_id))
    
    return redirect('/')

def delete_dojo(request):
    dojo_id = request.POST['dojo_id']
    dojo = Dojo.objects.get(id=dojo_id)
    dojo.delete()
    return redirect('/')