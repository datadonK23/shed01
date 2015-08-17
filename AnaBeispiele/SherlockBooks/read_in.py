"""
Name: read_in
Purpose: Read in raw text from books, tokenize and write to pickle file
Author: Thomas Treml (datadonk23@gmail.com)
Date: 17.08.2015
"""

import cPickle
import nltk
from nltk.corpus import stopwords
nltk.data.path.append("/home/donk23/Workspace/nltk_data/")
from nltk import word_tokenize
import re

# Stop Words Collection
stop = []
stopwords_dict = nltk.corpus.stopwords.words("english")
for word in stopwords_dict:
    stop.append(unicode(word))
custom_stopwords = [u"the"]
for word in custom_stopwords:
    stop.append(word)

def clean_raw_text(txt_file, stopwords=stop):
    clean_tokens = []
    for line in f.readlines():
        st_line = line.decode("utf-8-sig").strip()
        if st_line == "":
            continue
        else:
            tokens = word_tokenize(st_line)
            for tok in tokens:
                cl_tok = re.sub(r"[^A-Za-z]" , "", tok)
                if cl_tok != "":
                    if cl_tok.lower() not in stopwords:
                        clean_tokens.append(cl_tok.lower())
    return clean_tokens

with open("./data/SherlockHolmes-ProjektGutenberg/sh12.txt") as f:
    txt_12 = clean_raw_text(f, stop)
    cPickle.dump(txt_12, open("./data/txt_12.p", "wb"))
with open("./data/SherlockHolmes-ProjektGutenberg/sh06.txt") as f:
    txt_06 = clean_raw_text(f, stop)

