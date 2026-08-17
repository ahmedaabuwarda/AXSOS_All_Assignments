from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

# Create your views here.
def index(request):
    return HttpResponse("This is the equivalent of @app.route('/') in Flask. This is the index page.")

def numbers(request, num):
    return JsonResponse({"data":"This is the equivalent of @app.route('/<int:num>') in Flask. This is the number page. The number is: {num}"})
