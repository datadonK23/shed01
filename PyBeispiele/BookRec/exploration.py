"""
Name: 
Purpose: Explore Data
Author: Thomas Treml (datadonk23@gmail.com)
Date: 
"""

import numpy as np
import pandas as pd

raw_users = pd.read_csv("./data/BX-Users.csv", sep=";")
print raw_users.head()
print raw_users.tail(2)
print raw_users.count()

raw_ratings = pd.read_csv("./data/BX-Book-Ratings.csv", sep=";")
print raw_ratings.head()
print raw_ratings.tail(2)
print raw_ratings.count()

raw_books = pd.read_csv("./data/BX-Books.csv", sep=";", error_bad_lines=False) # 22 books skipped
print raw_ratings.head()
print raw_ratings.tail(2)
print raw_books.count()
