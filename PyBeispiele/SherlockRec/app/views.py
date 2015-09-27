"""
Views
"""

from flask import render_template, request, redirect, url_for
from app import app
import models
#import controller

import json
import collections

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
    db_connection = models.DB()
    all_books = db_connection.get_books()

    # make list of book titles for UI
    for title in all_books.TITLE:
        bookTitles.append(title)

    # fetch inputs and send to recommendation scope
    if request.args:
        for i in range(1, len(bookTitles) + 1):
            ratings[str(i)] = request.args.get("IN"+str(i))
        return redirect(url_for("recommendation", ratings=ratings))
    else:
        return render_template("survey.html", bookTitles=bookTitles)


@app.route("/recommendation/<ratings>/")
@app.route("/recommendation")
def recommendation(ratings=None):
    if ratings: # ratings string received
        global user_rating_list
        user_rating_list = [] # list of ints for recommendation engine

        # process ratings string to json to list in correct order
        json_acceptable_string = ratings.replace("'", "\"").replace("u", "")
        input_dict = json.loads(json_acceptable_string)
        input_ordered = collections.OrderedDict(sorted(input_dict.items(), key=lambda x: int(x[0])))
        for k,v in input_ordered.items():
            user_rating_list.append(int(input_ordered[k]))

        return redirect(url_for("recommendation"))

    if user_rating_list: # make recommendation
        # fetch rating data from DB
        db_connection = models.DB()
        collaborative_data = db_connection.get_ratings()
        # fetch book data from DB
        db_connection = models.DB()
        all_books = db_connection.get_books()

        # make recommendation
        rec_engine = models.RecommendationEngine(user_rating=user_rating_list, collaborative_data=collaborative_data)
        recommendation = rec_engine.recommend_books()
        print recommendation

        # prepare output
        #FIXME loop
        top1_rec_title = all_books.loc[recommendation[0][0]].TITLE
        top2_rec_title = all_books.loc[recommendation[1][0]].TITLE
        top3_rec_title = all_books.loc[recommendation[2][0]].TITLE
        titlesRecomm = [top1_rec_title, top2_rec_title, top3_rec_title]
        top1_rec_score = recommendation[0][1]
        top2_rec_score = recommendation[1][1]
        top3_rec_score = recommendation[2][1]
        scoresRecomm = [top1_rec_score, top2_rec_score, top3_rec_score]
    else:
        titlesRecomm = ["Invalid Input"]
        scoresRecomm = ["NA"]

    #FIXME store rating
    return render_template("recommendation.html", recomm_out=zip(titlesRecomm, scoresRecomm))


#FIXME
@app.route("/ref")
def ref():
    return render_template("ref.html")