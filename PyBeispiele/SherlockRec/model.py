"""
Name: model
Purpose: Analytical model for collaborative filtering
Author: Thomas Treml (datadonk23@gmail.com)
Date: 2015-08-26
"""

import numpy as np
import pandas as pd
from sklearn.metrics import euclidean_distances, jaccard_similarity_score
from sklearn.cross_validation import train_test_split
import cPickle

# Load pre-loaded dataframes and explore
books_df = cPickle.load(open("./data/books_df.p", "rb"))
ratings_df = cPickle.load(open("./data/ratings_df.p", "rb"))
ratings_df.replace(np.nan, 0, inplace=True)

# train-test-split
train_df, test_df = train_test_split(ratings_df, test_size=0.2)

# dummy ratings
my_rating = [3., 4., 5., 3., 0., 4., 3., 0., 0., 0., 0., 0., 0., 0., 0.]
dummy_rating = list(np.random.randint(0, 6, size=15))

""" Similarity Measurement """
# Euclidean Distance
#eucldissk_12 = euclidean_distances(my_rating, vec1)

# Pearson
#r = np.corrcoef(my_rating, list(vec1))
#print r[0, 1]

# Jaccard
#js = jaccard_similarity_score(my_rating, list(vec1))
#print js


def all_books_recommendation(user_rating=my_rating, ratings_data=train_df, method=np.corrcoef):
    """
    Recommendation engine based on collaborative filtering

    :param user_rating: list of user inputs. Size 15, nan replaced with 0
    :param ratings_data: dataframe with user ratings about the 15 books
    :param method: similarity measurement method. Pearsons R (default), Jaccard similarity score and Euclidean distance
                    also possible
    :return: array of recommendation ratings for all 15 books
    """
    ratings_matrix = ratings_data.ix[: , "RAT_B01":"RAT_B15"].as_matrix()
    weighted_ratings = np.array([]); similarities = np.array([])
    for row in ratings_matrix:
        sim = method(user_rating, list(row))
        if sim.size > 1: # pearson
            sim = sim[0,1]
        else:
            sim = float(sim)
        weighted_row = row * sim
        row[row!=0.] = sim
        if weighted_ratings.size == 0 and similarities.size == 0:
            weighted_ratings = np.hstack((weighted_ratings, weighted_row))
            similarities = np.hstack((similarities, row))
        else:
            weighted_ratings = np.vstack((weighted_ratings, weighted_row))
            similarities = np.vstack((similarities, row))
    rat_sum = np.sum(weighted_ratings, axis=0)
    sim_sum = np.sum(similarities, axis=0)
    recommendation_array = rat_sum / sim_sum
    return recommendation_array

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
    for id,rating in zip(recommended_idx, recommended_ratings):
        recommended_dict[id] = rating
    return sorted(recommended_dict.items(), key=lambda x: x[1], reverse=True)



recommended_books, recommended_ratings = filter_recommendation(all_books_recommendation(ratings_data=ratings_df,
                                                                                        method=jaccard_similarity_score), my_rating)
my_recommdendation = sort_recommendation(recommended_books, recommended_ratings)
print my_recommdendation

def compare_method(test_rating_df=test_df):
    all_test_data = test_rating_df.ix[:, "RAT_B01":"RAT_B15"]
    random_rating = all_test_data.sample(1)
    print "test vector: "
    test_input =  random_rating.values.tolist()[0]
    print test_input
    recomm1 = all_books_recommendation(test_input)
    recomm2 = all_books_recommendation(test_input, method=jaccard_similarity_score)
    recomm3 = all_books_recommendation(test_input, method=euclidean_distances)
    #print recomm1
    #print recomm2
    #print recomm3
    #FIXME

#print compare_method()

