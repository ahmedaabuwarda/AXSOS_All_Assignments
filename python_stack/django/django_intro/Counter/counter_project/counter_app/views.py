from django.shortcuts import render

# Create your views here.
def index(request):
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1

    return render(request, 'index.html', {'count': request.session['count']})

def increment(request):
    if request.POST.get('count') == None or request.POST.get('count') == '':
        count = 0
    else:
        count = int(request.POST.get('count', 0))

    if 'count' in request.session:
        request.session['count'] += count
    else:
        request.session['count'] = count

    return render(request, 'index.html', {'count': request.session['count']})

def incrementByTwo(request):
    if 'count' in request.session:
        request.session['count'] += 2
    else:
        request.session['count'] = 2

    return render(request, 'index.html', {'count': request.session['count']})

def destroy_session(request):
    if 'count' in request.session:
        del request.session['count']
    return render(request, 'index.html', {'count': 0})
