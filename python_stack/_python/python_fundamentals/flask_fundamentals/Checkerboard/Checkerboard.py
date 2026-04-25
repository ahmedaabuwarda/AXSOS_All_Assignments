from flask import Flask, render_template

app = Flask(__name__)

@app.get('/')
def checkerboard8x8(x=8,y=8,color1="#fefae0",color2="#556b2f"):
    return render_template('index.html', color1=color1, color2=color2, x=int(x), y=int(y))

@app.get('/<int:y>')
def checkerboard8xY(x=8, y=8, color1="#fefae0", color2="#556b2f"):
    return render_template('index.html', color1=color1, color2=color2, x=int(x), y=int(y))

@app.get('/<int:x>/<int:y>')
def checkerboardXxY(x=8, y=8, color1="#fefae0", color2="#556b2f"):
    return render_template('index.html', color1=color1, color2=color2, x=int(x), y=int(y))

@app.get('/<int:x>/<int:y>/<color1>/<color2>')
def checkerboardXxYColor1Color2(x=8, y=8, color1="#fefae0", color2="#556b2f"):
    return render_template('index.html', color1=str(color1), color2=str(color2), x=int(x), y=int(y))

@app.errorhandler(404)
def error404(error):
    return "Sorry! Not found!"

if __name__ == "__main__":
    app.run(debug=True)