"""
Name: model
Purpose: Analytical model for collaborative filtering
Author: Thomas Treml (datadonk23@gmail.com)
Date: 2015-08-24
"""

import numpy as np
import pandas as pd
import cPickle

# Load pre-loaded dataframes and explore
books_df = cPickle.load(open("./data/books_df.p", "rb"))
print books_df.head()
ratings_df = cPickle.load(open("./data/ratings_df.p", "rb"))
print ratings_df.describe()

#FIXME
