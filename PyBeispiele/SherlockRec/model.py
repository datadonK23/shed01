"""
Name: model
Purpose: Analytical model for collaborative filtering
Author: Thomas Treml (datadonk23@gmail.com)
Date: 2015-08-31
"""

import numpy as np
import pandas as pd
from sklearn.metrics import jaccard_similarity_score
from sklearn.cross_validation import train_test_split
import cPickle

# Load pre-loaded dataframes and explore
books_df = cPickle.load(open("./data/books_df.p", "rb"))
ratings_df = cPickle.load(open("./data/ratings_df.p", "rb"))

# train-test-split
train_df, test_df = train_test_split(ratings_df, test_size=0.2)

# dummy ratings
my_rating = [-1, 1, 1, -1, 0., 1, -1, 0., 0., 0., 0., 0., 0., 0., 0.]
dummy_rating = list(np.random.randint(-1, 1, size=15))

""" Similarity Measurement """
def all_books_recommendation(user_rating=my_rating, ratings_data=ratings_df, method=jaccard_similarity_score):
    """
    Recommendation engine based on collaborative filtering. Creates recommendation array summing up weighted similarity
    scores by book, divided by sum of user similarities per rating.

    :param user_rating: list of user inputs. Size 15, nan replaced with 0
    :param ratings_data: dataframe with user ratings about the 15 books
    :param method: similarity measurement method. Jaccard similarity (default)
    :return: array of recommendation ratings for all 15 books
    """
    ratings_matrix = ratings_data.ix[: , "RAT_B01":"RAT_B15"].as_matrix().astype(float)
    weighted_ratings = np.array([]); user_similarities = np.array([])
    for row in ratings_matrix:
        similarity_coefficient = method(user_rating, row)
        weighted_row = row * similarity_coefficient
        row[row != 0.] = similarity_coefficient
        if weighted_ratings.size == 0 and user_similarities.size == 0:
            weighted_ratings = np.hstack((weighted_ratings, weighted_row))
            user_similarities = np.hstack((user_similarities, row))
        else:
            weighted_ratings = np.vstack((weighted_ratings, weighted_row))
            user_similarities = np.vstack((user_similarities, row))
    total = np.sum(weighted_ratings, axis=0)
    sim_sum = np.sum(user_similarities, axis=0)
    return total / sim_sum

def filter_recommendation(recommendation, user_input=my_rating):
    """
    Filter recommendation array based on input books

    :param recommendation: recommendation array of unsorted recommendation values
    :param user_input: list from user input
    :return: tuple ([index of recommended books],[ratings of recommended books])
    """
    recommend_books = []
    recommend_books_ratings = []
    for position, item in enumerate(user_input):
        if item == 0:
            recommend_books.append(position)
    for book_id in  recommend_books:
        recommend_books_ratings.append(recommendation[book_id])
    return recommend_books, recommend_books_ratings

def sort_recommendation(recommended_idx, recommended_ratings):
    """
    Sort recommendation based on rating values

    :param recommended_idx: list of book indices from recommendation
    :param recommended_ratings: list of ratings from recommendation
    :return: list of sorted recommendations - tuple of (book_id, rating)
    """
    recommended_dict = {}
    for id, rating in zip(recommended_idx, recommended_ratings):
        recommended_dict[id] = rating
    return sorted(recommended_dict.items(), key=lambda x: x[1], reverse=True)

recommended_books, recommended_ratings = filter_recommendation(all_books_recommendation(my_rating, ratings_data=train_df))

my_recommdendation = sort_recommendation(recommended_books, recommended_ratings)
print my_recommdendation

