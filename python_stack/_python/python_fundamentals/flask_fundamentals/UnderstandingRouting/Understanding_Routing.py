from flask import Flask

app = Flask(__name__)

@app.get('/')
def hellow_world():
    return "Hello World!"

@app.get('/Champion')
def champion():
    return "Champion"

@app.get('/say/<name>')
def handle(name):
    return f"Hi {name}!"

@app.get('/repeat/<int:num>/<word>')
def repeat(num, word):
    num = int(num)
    return f"{word}, "*num

@app.errorhandler(404)
def error404(error):
    return "Sorry! No response. Try again."


if __name__ == "__main__":
    app.run(debug=True)