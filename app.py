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

# Create Plot Figure
@app.callback(
    Output("data-plot", "figure"),
    [Input("upload-data", "contents")],
    [State("upload-data", "filename"), State("upload-data", "last_modified")],
)
def update_output(content, name, date):
    if content is not None:
        df = analysis_functions.parse_contents(content, name, date)
        data, layout = analysis_functions.setup_graph(df)
        return {"data": data, "layout": layout}
    else:
        return {"data": []}


# Create Data Table
@app.callback(
    Output("data-table-div", "children"),
    [Input("upload-data", "contents")],
    [State("upload-data", "filename"), State("upload-data", "last_modified")],
)
def update_output(content, name, date):
    if content is not None:
        df = analysis_functions.parse_contents(content, name, date)
        df.reset_index(inplace=True)
        return [
            dash_table.DataTable(
                style_data={"whiteSpace": "normal", "height": "auto"},
                style_table={"maxHeight": "300px", "overflowY": "scroll"},
                id="table",
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.to_dict("records"),
            )
        ]


if __name__ == "__main__":
    app.run_server(debug=True)
