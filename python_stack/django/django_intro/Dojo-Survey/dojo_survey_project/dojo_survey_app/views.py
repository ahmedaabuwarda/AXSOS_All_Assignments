from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def result(request):
    if request.method == "POST":
        name = request.POST.get('name')
        location = request.POST.get('location')
        language = request.POST.get('language')
        comment = request.POST.get('comment')

        request.session['name'] = name
        request.session['location'] = location
        request.session['language'] = language
        request.session['comment'] = comment

        context = {
            'name': name,
            'location': location,
            'language': language,
            'comment': comment
        }

        return render(request, 'result.html', context)
    
    return render(request, 'result.html')