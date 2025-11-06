from flask import Flask, redirect, request, render_template
from counter import Counter

app = Flask(__name__)
cnt = Counter()

@app.route("/")
def index():
    return render_template("index.html", value=cnt.value)

@app.route("/increment", methods=["POST"])
def increment():
    cnt.increase()
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    cnt.reset()
    return redirect("/")

@app.route("/set_value", methods=["POST"])
def set_value():
    try: 
        value = int(request.form['new_value'])
        cnt.set_value(value)
        return redirect("/")
    except:
        return redirect("/")
