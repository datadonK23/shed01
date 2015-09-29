"""
Views
"""

from flask import render_template, request, redirect, url_for
from app import app
import models

import json
import collections

rating_to_process = None

# MAIN page
@app.route("/")
def index(): 
    return render_template("index.html")

# SURVEY page
@app.route("/survey")
def survey():
    global bookTitles
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


# RECOMMENDATION page
@app.route("/recommendation/<ratings>/")
@app.route("/recommendation")
def recommendation(ratings=None):
    if ratings: # ratings string received
        global user_rating_list
        user_rating_list = [] # list of ints for recommendation engine
        global ratings_count
        ratings_count = 0

        # process ratings string to json to list in correct order
        json_acceptable_string = ratings.replace("'", "\"").replace("u", "")
        input_dict = json.loads(json_acceptable_string)
        input_ordered = collections.OrderedDict(sorted(input_dict.items(), key=lambda x: int(x[0])))
        for k,v in input_ordered.items():
            if int(input_ordered[k]) != 0:
                ratings_count += 1
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
        recommendation = rec_engine.recommend_books() # [(book_id, similarity_score)]
        print "Recommendation: " + str(recommendation)

        # prepare output
        titlesRecomm = []
        scoresRecomm = []
        for i in range(len(recommendation)):
            titlesRecomm.append(all_books.loc[recommendation[i][0]].TITLE)
            scoresRecomm.append("%.4f" % recommendation[i][1])

        # store user rating in db only if ratings count is > 2
        if ratings_count > 2:
            db_connection = models.DB()
            insert_confirmation = db_connection.insert_user_rating(user_rating_list)
            print insert_confirmation
        else: # show warning message
            warning_msg = zip(["zu wenige Bewertungen"], ["probier es noch einmal"])
            return render_template("recommendation.html", recomm_out=warning_msg)

    else: # if something unexpected went wrong
        titlesRecomm = ["Invalid Input"]
        scoresRecomm = ["probier es noch einmal"]

    return render_template("recommendation.html", recomm_out=zip(titlesRecomm, scoresRecomm))


# REFERENCES page
@app.route("/references")
def ref():
    return render_template("ref.html")