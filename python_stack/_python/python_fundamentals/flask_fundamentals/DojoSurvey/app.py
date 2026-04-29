from flask import Flask, request, render_template, session, redirect

app = Flask(__name__)

app.secret_key = "my_new_secret_key_is_dump"

@app.get('/')
def home():
    return render_template("index.html")

@app.post('/handle_form')
def handle_form():
    session["name"] = request.form["name"]
    session["language"] = request.form["language"]
    session["location"] = request.form["location"]
    session["gender"] = request.form["gender"]
    session["comment"] = request.form["comment"]
    session["terms"] = request.form["terms"]

    return redirect("/result")

@app.get('/result')
def result():
    return render_template('result.html')

@app.errorhandler(404)
def error404(error):
    return "Sorry!"

if __name__ == "__main__":
    app.run(debug=True)