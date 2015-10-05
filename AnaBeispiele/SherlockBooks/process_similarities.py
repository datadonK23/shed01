"""
Name: 
Purpose: 
Author: Thomas Treml (datadonk23@gmail.com)
Date: 
"""

import cPickle
import numpy as np
import pandas as pd
import matplotlib

path_similarities_file = "./data/similarities.p"

with open(path_similarities_file, "rb") as f:
    df = cPickle.load(f)
df.columns = ["SimScore"]

#remore perfect matches
df = df[df.SimScore < 0.99]
sorted_df = df.sort(["SimScore"], ascending=False)

plt = sorted_df.plot(use_index=False, grid=True, xticks=[0,5, 10,20,50,105])

sorted_df.head(n=10).to_html()