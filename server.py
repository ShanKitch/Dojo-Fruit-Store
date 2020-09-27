from flask import Flask, render_template, request, redirect
import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    first_name=request.form['first_name']
    last_name=request.form['last_name']
    student_id=request.form["student_id"]
    strawberry=request.form["strawberry"]
    raspberry=request.form["raspberry"]
    apple=request.form["apple"]
    blackberry=request.form["blackberry"]
    count= int(strawberry)+int(raspberry)+int(apple)+int(blackberry)
    now=datetime.datetime.now()
    timestamp=now.strftime("%B %d %Y %I:%M %p")
    print(request.form)
    print(f"Charging { first_name } { last_name } for { count } fruit") 
    return render_template("checkout.html", first_name=first_name,last_name=last_name,student_id=student_id,strawberry=strawberry,raspberry=raspberry, apple=apple, blackberry=blackberry,count=count,timestamp=timestamp)


if __name__=="__main__":   
    app.run(debug=True)    