"""
Views
"""

from flask import render_template, request
from app import app#, connection
#from models import Features

# main page
@app.route("/")
def index(): 
    return render_template("index.html")

@app.route("/survey")
def survey():
    return render_template("survey.html")

@app.route("/ref")
def ref():
    return render_template("ref.html")

#FIXME
@app.route("/recommend")
def recommend():
    return render_template("index.html")

#FIXME
@app.route("/result")
def result():
    return render_template("index.html")
