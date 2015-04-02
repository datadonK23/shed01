# -*- coding: utf-8 -*-
"""
Titel: FlaskReporting Data Analysis
Purpose: Analyse data about new constructed buildings in Austria between 
         1979 and 2002 
Author: Thomas Treml (datadonk23@gmail.com)
Date: August 2014
"""

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

pd.options.display.float_format = "{:,.2f}".format

# read in raw data
raw7079 = pd.read_csv("./data/wohngeb_70-79_proc.csv", sep = ";")
raw8002 = pd.read_csv("./data/wohngeb_80-02_proc.csv", sep = ";")
raw_total = pd.concat([raw7079,raw8002], ignore_index=True)

# data cleaning and merging
data = raw_total.loc[:,['\ufeff"Zeit"',"Anzahl Gebäude"]]
data.columns = ["Jahr", "Anzahl"]
data.loc[:,"Anzahl"] = data.loc[:,"Anzahl"] * 1000
data.loc[:,"Anzahl"] = data.loc[:,"Anzahl"].astype(int)

# investigate data
def datatable(data=data):
    # raw data plot, split for viz
    split_df = np.array_split(data, 2)
    return (split_df[0].transpose(), split_df[1].transpose())
    
def sum_plot(data=data):
    # summary statistics plot
    summary = pd.DataFrame(data.Anzahl.describe())
    summary.columns = ["Values"]
    return summary


def make_plot(data=data):
    # plot values and regression line to file   
    # glm
    slope, intercept, r_value, p_value, std_err = stats.linregress(data.Jahr, 
                                                                   data.Anzahl)
    line = slope * data.Jahr + intercept

    # plot
    plt.plot(data.Jahr, data.Anzahl,'-bo')
    plt.plot(data.Jahr, line,'r--', lw=3)
    plt.xlabel("Jahr", fontsize="large")
    plt.ylabel("Gebäude", fontsize="large")
    plt.title("Fertiggestellte Gebäude mit Wohnungen")
    #plt.show()
    plt.savefig("./static/IMG/plot.png")
