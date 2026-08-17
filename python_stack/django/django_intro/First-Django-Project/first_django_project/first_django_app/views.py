from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse

# Create your views here.
def root(request):
    return redirect('/blogs')

def index(request):
    return HttpResponse('Will be replaced with a list of blogs')

def new(request):
    return HttpResponse('Will be replaced with a form to create a new blog')

def create(request):
    return redirect('/blogs')

def show(request, blog_id):
    return HttpResponse(f'Will be replaced with a page to show blog number: {blog_id}')

def edit(request, blog_id):
    return HttpResponse(f'Will be replaced with a form to edit blog number: {blog_id}')

def destroy(request, blog_id):
    return redirect('/blogs')

def json(request):
    return JsonResponse({
        "title": "My First Blog",
        "content": "This is the content of my first blog post.",
    })