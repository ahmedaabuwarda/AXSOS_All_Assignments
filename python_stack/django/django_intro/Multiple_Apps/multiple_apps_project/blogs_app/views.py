from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def new(request):
    return render(request, 'new.html')

def create(request):
    return redirect('/blogs')

def show(request, number):
    context = {
        'number': number
    }
    return render(request, 'show.html', context)

def edit(request, number):
    context = {
        'number': number
    }
    return render(request, 'edit.html', context)

def destroy(request, number):
    return redirect('/blogs')