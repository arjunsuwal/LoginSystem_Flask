from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello User! This is my first Flask app"

@app.route("/about")
def about():
    return "This is about us page"

@app.route("/contact")
def contact():
    return "This is contact us page"

@app.route("/submit",methods=["GET","POST"])
def submit():
    if request.method == "POST":
        return "You have sent a data from the form."
    
    else:
        return "You are just in the login page watching the form"