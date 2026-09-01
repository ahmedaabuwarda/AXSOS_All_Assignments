from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages

# Create your views here.
def root(request):
    return redirect('/shows')

def index(request):
    context = {
        "shows": Show.objects.all(),
    }
    return render(request,'shows/index.html', context)

def create(request):
    return render(request,'shows/create.html')

def store(request):

    #validation before storing the data
    errors = Show.objects.basic_validator(request.POST)

    if (len(errors) > 0):
        for key, val in errors.items():
            messages.error(request, val)

        return redirect(f'/shows/create')

    title = request.POST['title']
    network = request.POST['network']
    release_date = request.POST['release_date']
    desc = request.POST['desc']

    Show.objects.create(title=title,network=network, release_date=release_date, desc=desc)

    return redirect('/')

def edit(request, id):
    context = {
        "show": Show.objects.get(id=id),
    }
    return render(request,'shows/edit.html', context)

def update(request):
    errors = Show.objects.basic_validator(request.POST)
    show_id = request.POST['show_id']

    if (len(errors) > 0):
        for key, val in errors.items():
            messages.error(request, val)

        return redirect(f'/shows/{show_id}/edit')

    show = Show.objects.get(id=show_id)

    show.title = request.POST['title']
    show.network = request.POST['network']
    show.release_date = request.POST['release_date']
    show.desc = request.POST['desc']
    show.save()

    return redirect('/')

def show(request, id):
    context = {
        "show": Show.objects.get(id=id),
    }
    return render(request,'shows/show.html', context)

def delete(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect('/')
