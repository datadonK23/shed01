"""
Name: spyreTest
Purpose: Testing spyre module
Author: Thomas Treml (datadonk23@gmail.com)
Code derived from spyre example "Stocks with Bokeh Plots"
Date: 2015-05-19
"""


from spyre import server
import model

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import json
from datetime import datetime
try:
    import urllib2
except ImportError:
    import urllib.request as urllib2

from bokeh.resources import INLINE
from bokeh.resources import CDN
from bokeh.embed import components
from bokeh import plotting


class Spyre_app(server.Launch):
    title = "Sport"

    inputs = [{
        "input_type": "dropdown",
        "label": "Sportart",
        "options": [
            {"label": "Radfahren", "value": "GOOG"},
            {"label": "Schwimmen", "value": "YHOO"}],
        "variable_name": "ticker",
        "action_id": "update_data"
    }]

    controls = [{
        "control_type": "hidden",
        "label": "get historical stock prices",
        "control_id": "update_data"
    }]

    outputs = [{
        "output_type": "plot",
        "output_id": "plot",
        "control_id": "update_data",
        "tab": "Plot",
        "on_page_load": True},
        {"output_type": "table",
        "output_id": "table_id",
        "control_id": "update_data",
        "tab": "Table",
        "on_page_load": True},
        {"output_type": "html",
        "output_id": "html_id",
        "control_id": "update_data",
        "tab": "Bokeh",
        "on_page_load": True
    }]

    tabs = ["Tabelle", "Plot"]

    def getData(self, params):
        ticker = params['ticker']
        # make call to yahoo finance api to get historical stock data
        #api_url = 'https://chartapi.finance.yahoo.com/instrument/1.0/{}/chartdata;type=quote;range=3m/json'.format(ticker)
        #result = urllib2.urlopen(api_url).read()
        #data = json.loads(result.decode('utf-8').replace('finance_charts_json_callback( ','')[:-1])  # strip away the javascript and load json
        #self.company_name = data['meta']['Company-Name']
        #df = pd.DataFrame.from_records(data['series'])
        #df['Date'] = pd.to_datetime(df['Date'],format='%Y%m%d')
        df = model.get_data("cycling_coll.json")
        return df

    def getPlot(self, params):
        df = self.getData(params)
        #plt_obj = df.set_index('Date').drop(['volume'],axis=1).plot()
        #plt_obj.set_ylabel("Price")
        #plt_obj.set_title(self.company_name)
        plt_obj = df.plot()#set_index("Date").plot()
        fig = plt_obj.get_figure()
        return fig

    def getHTML(self,params):
        df = self.getData(params)  # get data
        try:
            bokeh_plot = plotting.line(df['Date'],df['close'], color='#1c2980', legend="close", x_axis_type = "datetime", title=self.company_name)
        except AttributeError:
            bokeh_plot = plotting.figure(x_axis_type='datetime', title=self.company_name)
            bokeh_plot.line(df['Date'],df['close'], color='#1c2980', legend="close")
        bokeh_plot.line(df['Date'],df['high'], color='#80641c', legend="high")
        bokeh_plot.line(df['Date'],df['low'], color='#80321c', legend="low")

        script, div = components(bokeh_plot, CDN)
        html = "%s\n%s"%(script, div)
        return html

    def getCustomJS(self):
        return INLINE.js_raw[0]

    def getCustomCSS(self):
        return INLINE.css_raw[0]

if __name__ == '__main__':
    app = Spyre_app()
    app.launch(port=9097)
