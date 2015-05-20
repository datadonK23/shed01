"""
Model
"""

import pandas as pd
from datetime import datetime, timedelta

def get_data(FILE):
    """
        Load data from json file. Clean data return DF.
    """
    DATA_PATH = "./data/" + FILE
    df = pd.read_json(DATA_PATH)

    # Cleaning
    df["distance"] = df["distance"].map(lambda x: float(x.split()[0]))
    df["time_proc"] = df["time"].map(lambda x: datetime.strptime(x, "%H:%M:%S"))
    df["time"] = df["time_proc"].map(lambda x: timedelta(hours=x.hour, minutes=x.minute, seconds=x.second))
    df.drop("time_proc", 1, inplace=True)

    return df

