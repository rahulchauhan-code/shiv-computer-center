from flask import Flask, render_template
from utils.data import data1

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", data=data1)


@app.route("/about")
def about():
    return render_template("about.html", data=data1)


@app.route("/services")
def services():
    return render_template("services.html", data=data1)


@app.route("/team")
def team():
    return render_template("team.html", data=data1)


@app.route("/blog")
def blog():
    return render_template("blog.html", data=data1)


@app.route("/contact")
def contact():
    return render_template("contact.html", data=data1)
