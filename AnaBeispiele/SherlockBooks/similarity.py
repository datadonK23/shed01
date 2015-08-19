"""
Name: Similarty
Purpose: Process similarities between Sherlock Holmes books
Author: Thomas Treml (datadonk23@gmail.com)
Date: 19.08.2015
"""

import os
import string
import itertools
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
filenames1 = []
similarity_list = []

# FIXME LOOP
for file in filenames_list:
    col_list = [file]
    filenames_list.remove(file)
    with open(path + "/" + file) as f:
            file1 = f.read()
            for other_filename in filenames_list:
                with open(path + "/" + other_filename) as of:
                    file2 = of.read()
                    simi = cosine_sim(file1, file2)
                    col_list.append(simi)
                similarity_list.append(col_list)

print similarity_list
len(similarity_list) == 120