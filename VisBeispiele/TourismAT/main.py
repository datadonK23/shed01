# -*- coding: utf-8 -*-
"""
Visualisierung von Nächtigungen in Ö

@author: Thomas Treml (datadonk23@gmail.com)
Date: 26.01.2015
"""

import pandas as pd
import numpy as np
import bokeh.plotting as bk
import bokeh.models as bkm

raw_data = pd.read_csv("./data/datensatz.csv", sep=";", usecols=[0,1,4])
raw_data.columns = ["month_raw", "state_raw", "Ueb"]

# Cleaning data
row_list = []
for name, group in raw_data.groupby(["month_raw", "state_raw"]):
    row = list(name + (sum(group.Ueb),))
    row_list.append(row)
    
clean_data = pd.DataFrame.from_records(row_list)
clean_data.columns = ["monat", "bl", "Uebernacht"]

# Decode state code
BL_CODE = ["W96-1", "W96-2", "W96-3", "W96-4", "W96-5", "W96-6", "W96-7",
           "W96-8", "W96-9"]
BL_LIST = ["Bgl", "Ktn", "Noe", "Ooe", "Sbg", "Stmk", "Tir", "Vbg", "Wien"]

for i in range(len(BL_LIST)):
    clean_data.loc[clean_data.bl == BL_CODE[i], "bl"] = BL_LIST[i]

# Decode time code
clean_data.index = clean_data.monat
clean_data = pd.DataFrame(clean_data, index=clean_data.index,
                          columns=["bl", "Uebernacht"])
clean_data.index = pd.Series(pd.to_datetime(clean_data.index, format="%Y%m"))
#clean_data.index = clean_data.index.to_period("m")

# Splitting df per state
grouped = clean_data.groupby("bl")
data ={}
for bl in BL_LIST:
    data[bl] = grouped.get_group(bl)

# Statistics
def descr_value(func, data_col):
    """ Method to provide values of descriptiv statistics
    Takes function name func (as str) and column of DF,
    returns well formatted value """
    if func == "mean":
        val = data_col.mean()
    elif func == "max":
        val = data_col.max()
    elif func == "std":
        val = data_col.std()
    else:
        val = np.nan
    return '{:,.2f}'.format(val)

# Plottings
TOOLS = "pan,wheel_zoom,box_zoom,reset,save"
BACKGROUND_PLOT = "#e1e1e1"
bk.output_file("output.html", title="test output")

fig = bk.Figure(x_axis_type = "datetime", tools=TOOLS,
                x_axis_label="Monat", y_axis_label="Nächtigungen in Tsd.",
                background_fill=BACKGROUND_PLOT)
fig.xgrid.grid_line_color="white"
fig.ygrid.grid_line_color="white"

"""# Plot Jahr BL
BL = "Wien"
BL_COLOR = "blue"
JAHR = 1982
plot_data = data[BL][str(JAHR)]

fig = bk.Figure(x_axis_type = "datetime", tools=TOOLS,
                x_range= None,               
                x_axis_label="Monat", y_axis_label="Nächtigungen in Tsd.",
                background_fill=BACKGROUND_PLOT)
fig.xgrid.grid_line_color="white"
fig.ygrid.grid_line_color="white"

fig.line(plot_data.index, plot_data.Uebernacht/1000, color=BL_COLOR, 
         legend=plot_data.bl[0].upper())

print "MW: " + descr_value("mean", plot_data.Uebernacht)
print "Max: " + descr_value("max", plot_data.Uebernacht)
print "StD: " + descr_value("std", plot_data.Uebernacht)
"""

""" #Plot Jahr
JAHR = 2014
COLORS = ("#e41a1c", "#377eb8", "#4daf4a", "#984ea3", "#ff7f00", "#ffff33",
          "#a65628", "#f781bf", "#999999") # Palette by colorbrewer2.org

for i in range(len(data)):
    plot_data = data[BL_LIST[i]][str(JAHR)]
    BL_COLOR = COLORS[i]
    fig.line(plot_data.index, plot_data.Uebernacht/1000, color=BL_COLOR,
             legend=plot_data.bl[0].upper())

print "MW: " + descr_value("mean", clean_data[str(JAHR)].Uebernacht)
print ("Max: " + descr_value("max", clean_data[str(JAHR)].Uebernacht) + " in" ) #FIXME
print "StD: " + descr_value("std", clean_data[str(JAHR)].Uebernacht)
"""

# Trend


BL = "Ooe"
BL_COLOR = "blue"
plot_data = data[BL]

fig = bk.Figure(x_axis_type = "datetime", tools=TOOLS,
                x_range= None,               
                x_axis_label="Monat", y_axis_label="Nächtigungen in Tsd.",
                background_fill=BACKGROUND_PLOT)
fig.xgrid.grid_line_color="white"
fig.ygrid.grid_line_color="white"

fig.line(plot_data.index, plot_data.Uebernacht/1000, color=BL_COLOR, 
         legend=plot_data.bl[0].upper())

x = np.array(range(len(plot_data)))
y = np.array(plot_data.Uebernacht)

(m,b)=np.polyfit(x, y, 1)
yp = np.polyval([m,b],x)


fig.line(plot_data.index, yp/1000, color="red", 
         legend="regr")


bk.show(bk.VBox(fig))


# FIXME total trend
clean_data["2012"].Uebernacht.mean()

"""x = np.linspace(-3, 3, 50)
y = np.exp(-x**2) + 0.1 * np.random.randn(50)
plt.plot(x, y, 'ro', ms=5)

spl = UnivariateSpline(x, y)
xs = np.linspace(-3, 3, 1000)
plt.plot(xs, spl(xs), 'g', lw=3)

spl.set_smoothing_factor(0.5)
plt.plot(xs, spl(xs), 'b', lw=3)
plt.show()
"""

""" *** TODO ***

Plot Trend, TREND '15

****************
"""