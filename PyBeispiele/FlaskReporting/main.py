# -*- coding: utf-8 -*-

"""
Titel: FlaskReporting
Purpose: Show how to make a simple data analysis report with Flask
Author: Thomas Treml (datadonk23@gmail.com)
Date: August 2014
"""

from flask import Flask, render_template, send_file
from flask.ext.bootstrap import Bootstrap
import pandas as pd
import numpy as np
import ana

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/report")
def report(): 
    sum_table = ana.sum_plot()
    ana.make_plot()
    return render_template("report.html", sumtable=sum_table.to_html())
 
@app.route("/data")
def reference():
    df1, df2 = ana.datatable()
    return render_template("data.html", df1=df1.to_html(), df2=df2.to_html())  

if __name__ == "__main__":
    app.run(debug=True)
