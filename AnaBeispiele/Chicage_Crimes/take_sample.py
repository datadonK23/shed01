"""
Name: 
Purpose: Sample crime data
Author: Thomas Treml (datadonk23@gmail.com)
Date: 2015-04-01
"""

import json
import os

sample_data = []

file = os.path.abspath("/mnt/dataVol/Daten/AnaDaten/crimes_data/crimes_chicago_sample.json")

print "start processing"

with open(file) as f:
    all_data = json.load(f)

print "finished"
print all_data

