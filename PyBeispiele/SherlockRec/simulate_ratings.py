"""
Name: simulate_ratings
Purpose: Create dummy data for a recommendation system based on collaborative filtering
Author: Thomas Treml (datadonk23@gmail.com)
Date: 31.08.2015
"""

import numpy as np
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, VARCHAR, TIMESTAMP


""" DB presets """
from instance.config import PG_USER, PG_PASSWORD
db_uri = "postgresql://" + PG_USER + ":" + PG_PASSWORD + "@localhost/shrecdb"
engine = create_engine(db_uri)
con = engine.connect()


""" Rating engine presets """
np.random.seed(23)
user_ids = range(0, 100)
book_ids = range(1, 16)


""" Ratings engine """
p_rating = [0.1, 0.6, 0.3] # p for -1 (dislike), 0 (no Rating), 1 (like)
sim_ratings = pd.DataFrame(columns=["USER_ID", "RATINGS"])
for user_id in user_ids:
    user_ratings = np.random.choice([-1., 0, 1.], size=15, p=p_rating)
    sim_ratings.loc[user_id] = user_id, user_ratings.astype(int)
print sim_ratings


""" Ratings table """
# Schema
metadata = MetaData()
ratings_table = Table("ratings", metadata,
                      Column("user_id", Integer, nullable=False, primary_key=True),
                      Column("rated_at", TIMESTAMP),
                      Column("rat_book_01", Integer), Column("rat_book_02", Integer), Column("rat_book_03", Integer),
                      Column("rat_book_04", Integer), Column("rat_book_05", Integer), Column("rat_book_06", Integer),
                      Column("rat_book_07", Integer), Column("rat_book_08", Integer), Column("rat_book_09", Integer),
                      Column("rat_book_10", Integer), Column("rat_book_11", Integer), Column("rat_book_12", Integer),
                      Column("rat_book_13", Integer), Column("rat_book_14", Integer), Column("rat_book_15", Integer),
                      )

# Insert ratings
i = 0
for rating in sim_ratings.RATINGS:
    print "insert rating: " + str(i)
    insert = ratings_table.insert().values(rat_book_01 = rating[0], rat_book_02 = rating[1], rat_book_03 = rating[2],
                                           rat_book_04 = rating[3], rat_book_05 = rating[4], rat_book_06 = rating[5],
                                           rat_book_07 = rating[6], rat_book_08 = rating[7], rat_book_09 = rating[8],
                                           rat_book_10 = rating[9], rat_book_11 = rating[10], rat_book_12 = rating[11],
                                           rat_book_13 = rating[12], rat_book_14 = rating[13], rat_book_15 = rating[14])
    con.execute(insert)
    i += 1
    print "insert done"

print "finished ratings insertion"


""" Book table """
titles = ["A Study In Scarlet", "The Sign of the Four", "The Adventures of Sherlock Holmes",
          "Memoirs of Sherlock Holmes", "The Return of Sherlock Holmes", "The Hound of the Baskervilles",
          "The Valley of Fear", "The Adventure of Wisteria Lodge", "The Adventure of the Cardboard Box",
          "The Adventure of the Red Circle", "The Adventure of the Bruce-Partington Plans",
          "The Adventure of the Dying Detective", "The Disappearance of Lady Frances Carfax",
          "The Adventure of the Devil's Foot", "His Last Bow"]

# Schema
books_table = Table("books", metadata,
                    Column("book_id", Integer, nullable=False, primary_key=True),
                    Column("title", VARCHAR)
                    )
# Insert books
i = 0
for title in titles:
    print "insert book: " + str(i)
    insert = books_table.insert().values(book_id=book_ids[i], title= title)
    con.execute(insert)
    i += 1
    print "insert done"

print "finished books insertion"

con.close()
print "database setup finished"