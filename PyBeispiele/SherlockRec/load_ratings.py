"""
Name: load_rartings
Purpose: Load ratings and books from DB
Author: Thomas Treml (datadonk23@gmail.com)
Date: 2015-08-24
"""

import numpy as np
import pandas as pd
from sqlalchemy import create_engine, sql
import cPickle

""" DB presets """
from instance.config import PG_USER, PG_PASSWORD
db_uri = "postgresql://" + PG_USER + ":" + PG_PASSWORD + "@localhost/shrecdb"
engine = create_engine(db_uri)
con = engine.connect()

""" Load ratings """
# DB query
query_ratings = "SELECT * FROM ratings"
all_ratings = con.execute(sql.text(query_ratings))

# Data processing
user_ids = []; ts = []; br01 = []; br02 = []; br03 = []; br04 = []; br05 = []; br06 = []; br07 = []; br08 = [];
br09 = []; br10 = []; br11 = []; br12 = []; br13 = []; br14 = []; br15 = []
for rating in all_ratings:
    user_ids.append(rating[0])
    ts.append(rating[1])
    br01.append(rating[2]); br02.append(rating[3]); br03.append(rating[4]); br04.append(rating[5]);
    br05.append(rating[6]); br06.append(rating[7]); br07.append(rating[8]);br08.append(rating[9]);
    br09.append(rating[10]); br10.append(rating[11]); br11.append(rating[12]); br12.append(rating[13]);
    br13.append(rating[14]); br14.append(rating[15]); br15.append(rating[16])

# Dataframe and save to pickle file
ratings = {"USER_ID": user_ids, "RATED_AT": ts, "RAT_B01": br01, "RAT_B02": br02, "RAT_B03": br03, "RAT_B04": br04,
           "RAT_B05": br05, "RAT_B06": br06, "RAT_B07": br07, "RAT_B08": br08, "RAT_B09": br09, "RAT_B10": br10,
           "RAT_B11": br11, "RAT_B12": br12, "RAT_B13": br13, "RAT_B14": br14, "RAT_B15": br15}
ratings_df = pd.DataFrame(ratings)
ratings_df.replace(0, np.nan, inplace=True)
cPickle.dump(ratings_df, open("./data/ratings_df.p", "wb"))

print "Ratings records: " + str(len(ratings_df))
print ratings_df.head()


""" Load books """
# DB query
query_books = "SELECT * FROM books"
books = con.execute(sql.text(query_books))
con.close()

# Data processing
book_ids = []; titles = []
for book in books:
    book_ids.append(book[0])
    titles.append(book[1])

# Dataframe and save to pickle file
books = {"BOOK_ID": book_ids, "TITLE": titles}
books_df = pd.DataFrame(books)
cPickle.dump(books_df, open("./data/books_df.p", "wb"))

print "Book records: " + str(len(books_df))
print books_df.head()
