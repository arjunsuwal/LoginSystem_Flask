from flask import Flask

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