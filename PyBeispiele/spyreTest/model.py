"""
Description: Model for App
Author: Thomas Treml (datadonk23@gmail.com)
Date: 2015-05-18
"""

import os
import pandas as pd
from datetime import datetime, timedelta

def get_data(FILE):
    DATA_PATH = "./data/" + FILE
    #os.path.join(os.path.dirname(os.path.realpath(__file__)), "data", "cycling_coll.json")
    df = pd.read_json(DATA_PATH)

    # Cleaning
    df["distance"] = df["distance"].map(lambda x: float(x.split()[0]))
    df["time_proc"] = df["time"].map(lambda x: datetime.strptime(x, "%H:%M:%S"))
    df["time"] = df["time_proc"].map(lambda x: timedelta(hours=x.hour, minutes=x.minute, seconds=x.second))
    df.drop("time_proc", 1)

    df = df[[1, 4, 2]]

    return df

