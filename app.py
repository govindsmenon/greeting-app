from flask import Flask, redirect, render_template, request, flash, url_for

app = Flask(__name__)

app.secret_key = "gsmsecret123"

@app.route("/")
def home():
    flash("Please type your name..")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greeting():
    if request.form["entered_name"]!="":
        flash("Hi "+str(request.form["entered_name"])+"! Nice to meet you !")
        return render_template("index.html")
    else:
        return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
