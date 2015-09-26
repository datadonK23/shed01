"""
Views
"""

from flask import render_template, request, redirect, url_for
from app import app#, connection
import models
import controller

import json
import re

rating_to_process = None

# main page
@app.route("/")
def index(): 
    return render_template("index.html")

@app.route("/survey")
def survey():
    bookTitles = []
    ratings = {}

    # fetch book data from DB
    DB = controller.DB_Connection()
    con = controller.DB_Connection.make_connection(DB)
    books_con = models.DB(con)
    all_books = books_con.get_books()
    controller.DB_Connection.close_connection(DB, con)

    # make list of book titles for UI
    for title in all_books.TITLE:
        bookTitles.append(title)

    # fetch inputs and send to recommendation scope
    if request.args:
        for i in range(1, len(bookTitles) + 1):
            ratings[str(i)] = request.args.get("IN"+str(i))
        #ratings["input_book01"] = request.args.get("INBook01")
        #ratings["input_book02"] = request.args.get("INBook02")
        #ratings["input_book03"] = request.args.get("INBook03")
        #print ratings
        return redirect(url_for("recommendation", ratings=ratings))
    else:
        return render_template("survey.html", bookTitles=bookTitles)


#FIXME
@app.route("/recommendation/<ratings>/")
@app.route("/recommendation")
def recommendation(ratings=None):
    if ratings:
        print ratings
        json_acceptable_string = ratings.replace("'", "\"").replace("u", "")
        #print json_acceptable_string
        input_dict = json.loads(json_acceptable_string)
        global rating_to_process
        rating_to_process = [input_dict["1"], input_dict["2"], input_dict["15"]]
        return redirect(url_for("recommendation"))

    if rating_to_process:
        test1 = str(int(rating_to_process[0])) + " ist der erste Wert"
        test2 = str(int(rating_to_process[1])) + " ist der zweite Wert"
        test3 = str(int(rating_to_process[2])) + " ist der letzte Wert"
        testRecomm = [test1, test2, test3]
    else:
        testRecomm = ["test123", "test456"]
    return render_template("recommendation.html", testRecomm=testRecomm)


#FIXME
@app.route("/ref")
def ref():
    return render_template("ref.html")