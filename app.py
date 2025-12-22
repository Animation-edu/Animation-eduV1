from flask import Flask, flash, redirect, render_template, request, session
app = Flask(__name__)

@app.route("/")
def index():
    #return homepage
    return render_template("index.html")

@app.route("/chemistry")
def chemistry():
    #return homepage
    return render_template("chemistry.html")