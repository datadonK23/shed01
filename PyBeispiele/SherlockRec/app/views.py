"""
Views
"""

from flask import render_template, request, redirect, url_for
from app import app#, connection
#from models import Features

# main page
@app.route("/")
def index(): 
    return render_template("index.html")

@app.route("/survey")
def survey():
    ratings = {}
    if request.args:
        ratings["input_book01"] = request.args.get("INBook01")
        ratings["input_book02"] = request.args.get("INBook02")
        ratings["input_book03"] = request.args.get("INBook03")
        #test print ratings
        return redirect(url_for("recommendation", ratings=ratings))
    else:
        return render_template("survey.html")


#FIXME
@app.route("/recommendation/<ratings>/")
@app.route("/recommendation")
def recommendation(ratings=None):
    if ratings:
        print ratings
        return redirect(url_for("recommendation"))
    return render_template("recommendation.html")


#FIXME
@app.route("/ref")
def ref():
    return render_template("ref.html")