"""
Description: Model for App
Author: Thomas Treml (datadonk23@gmail.com)
Date: 2015-05-18
"""

import os
import pandas as pd

DATA_PATH = "./data/cycling_coll.json" #os.path.join(os.path.dirname(os.path.realpath(__file__)), "data", "cycling_coll.json")

raw = pd.read_json(DATA_PATH)

# Cleaning
raw["distance"] = raw["distance"].map(lambda x: float(x.split()[0]))
