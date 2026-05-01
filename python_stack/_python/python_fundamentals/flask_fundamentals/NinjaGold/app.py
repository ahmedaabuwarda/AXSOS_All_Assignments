from flask import Flask, render_template, request, redirect, session
import random
import datetime

app = Flask(__name__)

app.secret_key = "this_is_secret_2_key"

@app.get('/')
def index():
    if session.get('gold') != None and session.get('activities') != None:
        gold = session.get('gold')
        activities = session.get('activities')
    else: 
        session['gold'] = 0
        session['activities'] = []
    
    gold = session.get('gold')
    activities = session.get('activities')

    return render_template("index.html", gold=gold, activities=activities, len=len(activities))

@app.post('/process_money')
def process_money():

    if session.get('gold') >= 500:
        return redirect('/')
    
    building = request.form['building']
    rand_gold_building_object = {
        "farm" : random.randint(10, 20),
        "cave" : random.randint(5, 10),
        "house" : random.randint(2,5),
        "casino" : random.randint(-50, 50)
    }

    gold_amount = rand_gold_building_object[building]
    
    date = datetime.datetime.now()
    activities, activity = session['activities'], ""

    if gold_amount < 0:
        activity = f"<li style='color: red;'>Entered a {building} and lost {abs(gold_amount)} golds!... Ouch.. ({date})</li>"
    else:        
        activity = f"<li style='color: green;'>Earned {gold_amount} from the {building}! ({date})</li>"

    activities.append(activity)
    session['activities'] = activities

    # if the gold is not in the session create one, if there add the gold to it
    if (session.get('gold') == None):
        session['gold'] = gold_amount
    else:
        session['gold'] += gold_amount
    
    gold = session['gold']
    activities = session['activities']

    return render_template("index.html", gold=gold, activities=activities, len=len(activities))

@app.get('/reset')
def clear():
    if session.get('gold') >= 500:
        session.clear()

    return redirect('/')

@app.errorhandler(404)
def notFound404(error):
    return "Opps! Not found!"

if __name__ == "__main__":
    app.run(debug=True)