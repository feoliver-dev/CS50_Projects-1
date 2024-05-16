from flask import Flask, Response, redirect, render_template, request

app = Flask(__name__)



@app.route("/")
def index():
        return render_template("index.html")

@app.route("/history")
def history():
        return render_template("history.html")

@app.route("/art")
def art():
        return render_template("art.html")

@app.route("/architecture")
def architecture():
        return render_template("architecture.html")

@app.route("/cinema")
def cinema():
        return render_template("cinema.html")


@app.route("/dance")
def dance():
        return render_template("dance.html")

@app.route("/literature")
def literature():
        return render_template("literature.html")

@app.route("/music")
def music():
        return render_template("music.html")

@app.route("/painting")
def painting():
        return render_template("painting.html")

@app.route("/sculpture")
def sculpture():
        return render_template("sculpture.html")

@app.route("/fashion")
def fashion():
        return render_template("fashion.html")

@app.route("/about")
def about():
        return render_template("about.html")
