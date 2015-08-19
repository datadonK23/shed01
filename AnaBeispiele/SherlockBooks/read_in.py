"""
Name: read_in
Purpose: Read in raw text from books, tokenize and write to pickle file
Author: Thomas Treml (datadonk23@gmail.com)
Date: 19.08.2015
"""

import cPickle
import re
from nltk import data
data.path.append("/home/donk23/Workspace/nltk_data/")
from nltk.corpus import stopwords
from nltk import word_tokenize


# Stopwords collection
stop = []
stopwords_dict = stopwords.words("english")
for word in stopwords_dict:
    stop.append(unicode(word))
custom_stopwords = [u"the"]
for word in custom_stopwords:
    stop.append(word)

# Tokenize text
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

# Tokenize text
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


# Tokenize raw books and save tokens as pickle file
with open("./data/SherlockHolmes-ProjektGutenberg/sh01.txt") as f:
    txt_01 = clean_raw_text(f, stop)
    cPickle.dump(txt_01, open("./data/txt_01.p", "wb"))
with open("./data/SherlockHolmes-ProjektGutenberg/sh02.txt") as f:
    txt_02 = clean_raw_text(f, stop)
    cPickle.dump(txt_02, open("./data/txt_02.p", "wb"))
with open("./data/SherlockHolmes-ProjektGutenberg/sh03.txt") as f:
    txt_03 = clean_raw_text(f, stop)
    cPickle.dump(txt_03, open("./data/txt_03.p", "wb"))
with open("./data/SherlockHolmes-ProjektGutenberg/sh04.txt") as f:
    txt_04 = clean_raw_text(f, stop)
    cPickle.dump(txt_04, open("./data/txt_04.p", "wb"))
with open("./data/SherlockHolmes-ProjektGutenberg/sh05.txt") as f:
    txt_05 = clean_raw_text(f, stop)
    cPickle.dump(txt_05, open("./data/txt_05.p", "wb"))
with open("./data/SherlockHolmes-ProjektGutenberg/sh06.txt") as f:
    txt_06 = clean_raw_text(f, stop)
    cPickle.dump(txt_06, open("./data/txt_06.p", "wb"))
with open("./data/SherlockHolmes-ProjektGutenberg/sh07.txt") as f:
    txt_07 = clean_raw_text(f, stop)
    cPickle.dump(txt_07, open("./data/txt_07.p", "wb"))
with open("./data/SherlockHolmes-ProjektGutenberg/sh08.txt") as f:
    txt_08 = clean_raw_text(f, stop)
    cPickle.dump(txt_08, open("./data/txt_08.p", "wb"))
with open("./data/SherlockHolmes-ProjektGutenberg/sh09.txt") as f:
    txt_09 = clean_raw_text(f, stop)
    cPickle.dump(txt_09, open("./data/txt_09.p", "wb"))
with open("./data/SherlockHolmes-ProjektGutenberg/sh10.txt") as f:
    txt_10 = clean_raw_text(f, stop)
    cPickle.dump(txt_10, open("./data/txt_10.p", "wb"))
with open("./data/SherlockHolmes-ProjektGutenberg/sh11.txt") as f:
    txt_11 = clean_raw_text(f, stop)
    cPickle.dump(txt_11, open("./data/txt_11.p", "wb"))
with open("./data/SherlockHolmes-ProjektGutenberg/sh12.txt") as f:
    txt_12 = clean_raw_text(f, stop)
    cPickle.dump(txt_12, open("./data/txt_12.p", "wb"))
with open("./data/SherlockHolmes-ProjektGutenberg/sh13.txt") as f:
    txt_13 = clean_raw_text(f, stop)
    cPickle.dump(txt_13, open("./data/txt_13.p", "wb"))
with open("./data/SherlockHolmes-ProjektGutenberg/sh14.txt") as f:
    txt_14 = clean_raw_text(f, stop)
    cPickle.dump(txt_14, open("./data/txt_14.p", "wb"))
with open("./data/SherlockHolmes-ProjektGutenberg/sh15.txt") as f:
    txt_15 = clean_raw_text(f, stop)
    cPickle.dump(txt_15, open("./data/txt_15.p", "wb"))
