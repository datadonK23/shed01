"""
Name: model
Purpose: Analytical model for collaborative filtering
Author: Thomas Treml (datadonk23@gmail.com)
Date: 2015-08-25
"""

import numpy as np
import pandas as pd
from scipy.spatial import distance
from scipy.stats import pearsonr
from sklearn.metrics import euclidean_distances, jaccard_similarity_score
import cPickle

# Load pre-loaded dataframes and explore
books_df = cPickle.load(open("./data/books_df.p", "rb"))
print books_df.head()
ratings_df = cPickle.load(open("./data/ratings_df.p", "rb"))
ratings_df.replace(np.nan, 0, inplace=True)
print ratings_df.describe()

vec1 = ratings_df.ix[0, 1:-1].values
vec2 = ratings_df.ix[1, 1:-1].values
vec3 = ratings_df.ix[2, 1:-1].values

""" Similarity Measurement """
# Euclidean Distance
eucldis_12 = distance.euclidean(vec1, vec2)
eucldis_23 = distance.euclidean(vec2, vec3)
eucldissk_12 = euclidean_distances(vec1, vec2)
eucldissk_23 = euclidean_distances(vec2, vec3)
print eucldis_12, eucldis_23
print eucldissk_12[0, 0], eucldissk_23[0, 0]

# Pearson
r_12 = np.corrcoef(list(vec1), list(vec2))
r_23 = np.corrcoef(list(vec2), list(vec3))
rsci_12 = pearsonr(vec1, vec2)
rsci_23 = pearsonr(vec2, vec3)
print r_12[0, 1], r_23[0, 1]
print rsci_12[0], rsci_23[0]

# Jaccard
js_12 = jaccard_similarity_score(list(vec1), list(vec2))
js_23 = jaccard_similarity_score(list(vec2), list(vec3))
print js_12, js_23


#FIXME
