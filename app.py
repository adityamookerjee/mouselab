# -*- coding: utf-8 -*-
"""
Preliminary 
"""
import flask
import dash
from dash.dependencies import Output, Input, State
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import scipy

# Custom Stuff
import app_layout
import analysis_functions

SERVER = flask.Flask(__name__)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], server=SERVER)
app.layout = html.Div(children=[app_layout.NAVBAR, app_layout.BODY])
app.title = "MouseLab"
# Callbacks

# Store Data
@app.callback(
    Output("data-store", "data"),
    [Input("upload-data", "contents")],
    [State("upload-data", "filename"), State("upload-data", "last_modified")],
)
def update_output(content, name, date):
    if content:
        df = analysis_functions.parse_contents(content, name, date)
        return df.to_dict("records")


# Create Plot Figure
@app.callback(Output("data-analysis-div", "children"), [Input("data-store", "data")])
def update_plot(store_data):
    if store_data:
        df = pd.DataFrame(store_data)
        data, layout = analysis_functions.setup_graph(df)
        return [dcc.Graph(id="plot", figure={"data": data, "layout": layout})]
    else:
        return []


# Create Data Table
@app.callback(
    [Output("data-table-div", "children"), Output("stats-table-div", "children")],
    [Input("data-store", "data")],
)
def update_data_table(store_data):
    if store_data:
        df = pd.DataFrame(store_data)
        return (
            [
                dash_table.DataTable(
                    style_data={"whiteSpace": "normal", "height": "auto"},
                    style_table={"maxHeight": "300px", "overflowY": "scroll"},
                    id="data-table",
                    columns=[{"name": i, "id": i} for i in df.reset_index().columns],
                    data=df.reset_index().to_dict("records"),
                )
            ],
            [
                dash_table.DataTable(
                    style_data={"whiteSpace": "normal", "height": "auto"},
                    style_table={"maxHeight": "300px", "overflowY": "scroll"},
                    id="stats-table",
                    columns=[{"name": i, "id": i} for i in df.describe().reset_index()],
                    data=df.describe().reset_index().to_dict("records"),
                )
            ],
        )
    else:
        return None, None


if __name__ == "__main__":
    app.run_server(debug=True)
