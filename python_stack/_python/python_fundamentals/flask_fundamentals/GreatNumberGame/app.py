from flask import Flask, render_template, redirect, session, request
import random

app = Flask(__name__)
app.secret_key = "This_is_again_secret_key"

@app.get('/')
def home():
    # random number
    random_number = 0
    if (session.get('random_number') == None):
        random_number = random.randint(1, 100)
        session['random_number'] = random_number
        
    return render_template('index.html', result="", color="red")

@app.post('/guess')
def guess():
    number = int(request.form.get('number'))
    random_number = int(session['random_number'])
    result, color = "", "red"
    if (random_number > number):
        result = "Too low!"
    elif (random_number < number):
        result = "Too high!"
    else:
        result = "Good job!"
        color = "green"
    
    return render_template('index.html', result=result, color=color)

@app.get('/again')
def clear():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)