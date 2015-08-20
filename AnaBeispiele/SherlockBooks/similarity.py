"""
Name: Similarty
Purpose: Process similarities between Sherlock Holmes books
Author: Thomas Treml (datadonk23@gmail.com)
Date: 20.08.2015
"""

import os
import string
import cPickle
import pandas as pd
from nltk import data
data.path.append("/home/donk23/Workspace/nltk_data/")
from nltk.corpus import stopwords
from nltk import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer


# Stopwords collection and punctuation map
stop = []
stopwords_dict = stopwords.words("english")
for word in stopwords_dict:
    stop.append(unicode(word))
custom_stopwords = [u"the"]
for word in custom_stopwords:
    stop.append(word)

punctuation_map = dict((ord(punct), None) for punct in set(string.punctuation))

# Tokenize and text cleaning
def tokenize(text):
    return word_tokenize(text.lower().translate(punctuation_map))

# Calculate cosine similarity
vectorizer = TfidfVectorizer(tokenizer=tokenize, stop_words=stop)

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]


# Read in files and calculate similarity matrix
path = "./data/SherlockHolmes-ProjektGutenberg"
book_pairs = [] # map for calculation
filenames_list = os.listdir(path)
filenames_list.remove("README.md")
for f1 in range(len(filenames_list)):
    for f2 in range(f1, len(filenames_list)):
        book_pairs.append((filenames_list[f1], filenames_list[f2]))
book_pairs.sort()

similarities = {}
for pair in book_pairs:
    with open(path + "/" + pair[0]) as f1:
        text1 = f1.read()
    with open(path + "/" + pair[1]) as f2:
        text2 = f2.read()
    similarities[pair] = cosine_sim(text1, text2)

# Make DF and write pickle
similarities_df = pd.DataFrame.from_dict(similarities, orient="index")

cPickle.dump(similarities_df, open("./data/similarities.p", "wb"))

print "finished"