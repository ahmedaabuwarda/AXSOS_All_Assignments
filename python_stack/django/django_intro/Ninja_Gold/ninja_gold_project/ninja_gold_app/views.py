import random
from datetime import datetime
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0

    if 'activities' not in request.session:
        request.session['activities'] = []

    if 'winning_score' not in request.session:
        request.session['winning_score'] = 200

    if 'winning_moves' not in request.session:
        request.session['winning_moves'] = 15

    if 'moves' not in request.session:
        request.session['moves'] = 0

    if 'winner' not in request.session:
        request.session['winner'] = ''
    

    return render(request, 'index.html')

def process_money(request):
    if 'gold' in request.session:
        if int(request.session['gold']) >= int(request.session['winning_score']) and int(request.session['winning_moves']) >= int(request.session['moves']):

            request.session['winner'] = True
            return redirect('/')
        elif int(request.session['gold']) >= int(request.session['winning_score']) and int(request.session['winning_moves']) < int(request.session['moves']):
            request.session['winner'] = False
            return redirect('/')


    action = request.POST['action']

    process = {
        "farm": random.randint(10, 20),
        "cave": random.randint(10, 20),
        "house": random.randint(10, 20),
        "quest": random.randint(-50, 50),
    }

    gold = process[action]
    color = "green" if gold > 0 else "red"

    time = datetime.now().strftime("%Y %m %d %H:%M:%S")
    request.session['gold'] += gold
    request.session['moves'] += 1

    request.session['activities'].insert(0, {"color": f'{color}', "data": f'You entered a {action} and earned {gold } gold. ({time})'})

    # print(gold)
    # print(request.session['activities'])
    # print(request.session['moves'])

    return redirect('/')

def destroy_session(request):
    request.session.flush()
    return redirect('/')