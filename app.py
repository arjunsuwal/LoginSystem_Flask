from flask import Flask, request, Response, redirect, url_for, session

app = Flask(__name__)
# Setting secretkey for sessions
app.secret_key = "Supersecret_of_You"

# homepage or login page
@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if username == "admin" and password == "123":
            session["user"] = username # Store in session
            return redirect(url_for("welcome"))
        
        else:
            return Response("Sorry!! In-valid Credentials please try it again.", mimetype="text/plain")
    
    return '''
            <h2> Login Page</h2>
            <form method="POST">
            Username: <input type="text" name="username"><br>
            Password: <input type="text" name="password"><br>
            <input type="submit" value="Login">
            </form>
'''

#Welcome page after login
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
        <h2> Welcome, {session["user"]}!</h2>
        <a href={url_for("logout")}>Logout</a>
        
    '''
    
    return redirect(url_for("login"))

#logout route
@app.route("/logout")
def logout():
    session.pop("user", None) #Clear the session of previous loged in user
    return redirect(url_for("login")) 