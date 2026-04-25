from flask import Flask, render_template

app = Flask(__name__)

@app.get('/play')
def play():
    times = 3
    color = "blue"
    return render_template("index.html", times=times, color=color)

@app.get('/play/<int:times>')
def play_times(times):
    color = "blue"
    return render_template("index.html", times=int(times), color=color)
    
@app.get('/play/<int:times>/<color>')
def play_times_color(times, color):
    return render_template("index.html", times=int(times), color=color)

@app.errorhandler(404)
def error404(error):
    return "Sorry! Wrong link. Try again!"

if __name__ == "__main__":
    app.run(debug=True)