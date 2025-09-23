from flask import Flask, render_template, request

app = Flask(__name__)


# homepage using html files instead of inline html
@app.route("/")
def login():
    return render_template("login.html")

# match the action and route extension
@app.route("/submit", methods=["POST"])
def submit():
    username= request.form.get("username") #getting name attribute from form 
    password= request.form.get("password")
    
    # if username =="arjun" and password=="pass":
    #     return render_template("welcome.html", name = username)
    
    valid_users={
        "arjun":"pass",
        "jaya":"baby",
        "honey":"123"
    }
    
    if username in valid_users and password==valid_users[username]:
        return render_template("welcome.html", name = username)
    
    else:
        return "Invalid Credentials"