"""
Name: model
Purpose: Analytical model for collaborative filtering
Author: Thomas Treml (datadonk23@gmail.com)
Date: 2015-08-26
"""

import numpy as np
import pandas as pd
#from scipy.spatial import distance
#from scipy.stats import pearsonr
from sklearn.metrics import euclidean_distances, jaccard_similarity_score
from sklearn.cross_validation import train_test_split
import cPickle

# Load pre-loaded dataframes and explore
books_df = cPickle.load(open("./data/books_df.p", "rb"))
#print books_df.head()
ratings_df = cPickle.load(open("./data/ratings_df.p", "rb"))
ratings_df.replace(np.nan, 0, inplace=True)
#print ratings_df.describe()

train_df, test_df = train_test_split(ratings_df, test_size=0.2)

vec1 = ratings_df.ix[0, 1:-1].values
my_rating = [3., 4., 5., 3., 0., 4., 3., 0., 0., 0., 0., 0., 0., 0., 0.]


""" Similarity Measurement """
# Euclidean Distance
#eucldissk_12 = euclidean_distances(my_rating, vec1)

# Pearson
#r = np.corrcoef(my_rating, list(vec1))
#print r[0, 1]

# Jaccard
#js = jaccard_similarity_score(my_rating, list(vec1))
#print js


def make_recommendation(user_rating=my_rating, ratings_data=train_df, method=np.corrcoef):
    """
        Make recommendation FIXME
    """
    ratings_matrix = ratings_data.as_matrix(["RAT_B01", "RAT_B02", "RAT_B03", "RAT_B04", "RAT_B05", "RAT_B06",
                                             "RAT_B07", "RAT_B08", "RAT_B09", "RAT_B10", "RAT_B11", "RAT_B12",
                                             "RAT_B13", "RAT_B14", "RAT_B15"])
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

recomm1 = make_recommendation()
recomm2 = make_recommendation(method=jaccard_similarity_score)
recomm3 = make_recommendation(method=euclidean_distances)
print recomm1
print recomm2
print recomm3

