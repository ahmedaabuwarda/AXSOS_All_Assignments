from flask import Flask

app = Flask(__name__)

@app.get('/')
def home_route():
    return "Here is home!"

@app.get('/hi')
def hi_route():
    return "Hi!"

@app.get('/users/<name>/<id>')
def get_user(name, id):
    return f"Found user: {name} - with id: {id}"

if  __name__ == "__main__":
    app.run(debug=True)
