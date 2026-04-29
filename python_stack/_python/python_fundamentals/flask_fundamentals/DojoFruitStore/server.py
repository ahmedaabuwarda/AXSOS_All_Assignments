from datetime import datetime

from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    data = request.form
    sum = int(data['strawberry']) + int(data['raspberry']) + int(data['apple'])
    print(f"Charging {data['first_name']} {data['last_name']} for {sum} fruit(s)!")
    date = datetime.now().strftime("%B %dth %Y %I:%M:%S %p")
    return render_template("checkout.html", data=data, sum=sum, date=date)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    