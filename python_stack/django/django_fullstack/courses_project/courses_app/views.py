from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course, Discription

# Create your views here.
def index(request):
    context = {
        "courses": Course.objects.all(),    
    }
    print(context)
    return render(request,'index.html', context)

def store(request):

    postData = request.POST

    course_errors = Course.objects.basic_validator(postData)
    desc_errors = Discription.objects.basic_validator(postData)

    if (len(course_errors) > 0 or len(desc_errors) > 0):

        for key, val in course_errors.items():
            messages.error(request, val)

        for key, val in desc_errors.items():
            messages.error(request, val)

        return redirect('/')

    name = request.POST['name']
    desc = request.POST['desc']

    course = Course.objects.create(name=name)
    Discription.objects.create(course=course, desc=desc)

    messages.success(request, 'Course created successfully!')
    return redirect('/')

def delete(request, id):
    context = {
        "course" : Course.objects.get(id=id)    
    }
    return render(request, 'delete.html', context)

def destroy(request):
    course_id = request.POST['course_id']
    course = Course.objects.get(id=course_id)
    course.delete()

    messages.success(request, 'Course deleted successfully!')

    return redirect('/')
