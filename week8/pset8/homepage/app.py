from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        return render_template("p1.html", instrument=request.form.get("Instrument"))

@app.route("/Hobbies")
def Hobbies():
    return render_template("p1.html")

@app.route("/CS50")
def CS50():
    return render_template("p2.html")


@app.route("/Duck")
def Duck():
    return render_template("p3.html")