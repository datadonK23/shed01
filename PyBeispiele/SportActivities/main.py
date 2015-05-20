"""
Name: Plotting Sport Activities
Purpose: Testing spyre
Author: Thomas Treml (datadonk23@gmail.com)
Code derived from spyre examples
Date: 2015-05-20
"""

from spyre import server
import model

class Spyre_app(server.Launch):
    title = "Sport Aktivit&auml;ten"

    inputs = [{
        "input_type": "dropdown",
        "label": "Sport",
        "options": [
            {"label": "Radfahren", "value": "cycling_coll.json"},
            {"label": "Schwimmen", "value": "swimming_coll.json"}],
        "variable_name": "sport_type",
        "action_id": "plot_activity_data"
    }]

    outputs = [{
        "output_type": "plot",
        "output_id": "plot_activity_data",
        "on_page_load": True
    }]

    def getData(self, params):
        """
            Get DF from model per sport. Process data and return DF ready for plotting.
        """
        file = params["sport_type"]
        df = model.get_data(file)
        df["distance"] = df["distance"] / 1000
        df["date"] = df["date"].map(lambda x: x.date())
        return df

    def getPlot(self, params):
        """
            Create plot and return plot figure
        """
        df = self.getData(params)
        plot = df.plot(x="date", y="distance", kind="bar",
                       legend=False, colormap="Pastel2")
        plot.set_ylabel("Distanz [km]")
        plot.set_xlabel("Datum")
        fig = plot.get_figure()
        return fig

if __name__ == '__main__':
    app = Spyre_app()
    app.launch(port=9097)
