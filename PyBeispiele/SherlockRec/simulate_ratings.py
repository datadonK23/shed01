"""
Name: simulate_ratings
Purpose: Create dummy data for a recommendation system based on collaborative filtering
Author: Thomas Treml (datadonk23@gmail.com)
Date: 21.08.2015
"""
from boto.beanstalk.exception import simple

import numpy as np
import pandas as pd

np.random.seed(23)

user_ids = range(0, 100)
book_ids = range(1, 16)

""" Ratings engine """
p_rating = [0.5, 0.05, 0.05, 0.1, 0.2, 0.1] # p for nan, [1:5] stars
sim_ratings = pd.DataFrame(columns=["USER_ID", "RATINGS"])
for user_id in user_ids:
    user_ratings = np.random.choice([0., 1. , 2., 3., 4., 5.], size=15, p=p_rating)
    user_ratings[user_ratings == 0] = np.nan
    sim_ratings.loc[user_id] = user_id, user_ratings
#print sim_ratings

""" Ratings table """
#FIXME

for rating in sim_ratings.RATINGS:
    print rating[0]

""" Book table """
titles = ["A Study In Scarlet", "The Sign of the Four", "The Adventures of Sherlock Holmes",
          "Memoirs of Sherlock Holmes", "The Return of Sherlock Holmes", "The Hound of the Baskervilles",
          "The Valley of Fear", "The Adventure of Wisteria Lodge", "The Adventure of the Cardboard Box",
          "The Adventure of the Red Circle", "The Adventure of the Bruce-Partington Plans",
          "The Adventure of the Dying Detective", "The Disappearance of Lady Frances Carfax",
          "The Adventure of the Devil's Foot", "His Last Bow"]

books = {"BOOK_ID": book_ids, "TITLE": titles}
books_df = pd.DataFrame(books)