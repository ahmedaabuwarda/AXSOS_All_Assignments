import random

from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    if 'guessed_number' not in request.session:
        # generate ranfom int between 1 to 100
        request.session['guessed_number'] = random.randint(1, 100)

    bg_color = "red"  # default background color

    return render(request, 'index.html', {'guessed_number': request.session['guessed_number'], 'bg_color': bg_color})

def guess(request):
    if request.method == 'POST':
        guessed_number = int(request.POST.get('guessed_number'))
        actual_number = request.session.get('guessed_number')

        bg_color = "red"  # default background color
        if guessed_number < actual_number:
            message = "Too low! Try again."
        elif guessed_number > actual_number:
            message = "Too high! Try again."
        else:
            message = f"{actual_number} was the number!"
            bg_color = "green"

        return render(request, 'index.html', {'message': message, 'guessed_number': actual_number, 'bg_color': bg_color})
    
    return render(request, 'index.html')

def play_again(request):
    # clear the session data
    request.session.flush()
    return redirect('index')