from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)

app.secret_key = "This_is_secret"

@app.get("/")
def index():
    if session.get("visit_counter") != None and session.get("increment_counter") != None:
        session["visit_counter"] += 1
        session["increment_counter"] += 1
    else:
        session["visit_counter"] = 1
        session["increment_counter"] = 1
    return render_template("index.html", visit_counter=session["visit_counter"], increment_counter=session["increment_counter"])

@app.post('/increment')
def increment():
    increment = int(request.form['increment'])
    session['increment_counter'] += increment
    return render_template("index.html", visit_counter=session["visit_counter"], increment_counter=session["increment_counter"])

@app.get('/increment2')
def increment2():
    session["increment_counter"] += 2
    return render_template("index.html", visit_counter=session["visit_counter"], increment_counter=session["increment_counter"])


@app.get('/destroy_session')
def destroy_session():#
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)