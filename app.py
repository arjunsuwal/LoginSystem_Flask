from flask import Flask, render_template, request

app= Flask(__name__)

#creating the routes now
@app.route("/feedback", methods=["POST", "GET"])
def feedback():
    if request.method == "POST":
        name = request.form.get("username")
        message= request.form.get("message")
        return render_template("thankyou.html", user=name, message=message)
    return render_template("feedback.html")

@app.route("/about")
def about():
    return render_template("about.html")