"""
Name: 
Purpose: 
Author: Thomas Treml (datadonk23@gmail.com)
Date: 
"""

import cPickle
txt_12 = cPickle.load(open("./data/txt_12.p", "rb"))

print txt_12[:5]
