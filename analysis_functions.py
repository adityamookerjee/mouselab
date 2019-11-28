import pandas as pd 
import plotly.graph_objs as go
import numpy as np
from scipy import stats
import base64
import io

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')),header=None,names=["Time","Grip Strength"])
            df.set_index("Time",inplace=True)
            return df

    except Exception as e:
        print(e)

def linear_fit(xi,y):
    """
    Uses scipy.stats to run OLS
    """
    # Generated linear fit
    slope, intercept, r_value, p_value, std_err = stats.linregress(xi,y)
    line = slope*xi+intercept
    return slope, intercept, r_value, p_value, std_err,line

def setup_graph(df):
    """
    Sets up a Graph of a Timeseries DataFrame.
    Returns data and layout
    """
    # Perform Stats Stuff
    slope, intercept, r_value, p_value, std_err,line = linear_fit(df.index,df.iloc[:,0].values)
    # Add a Trace of the Raw Data
    raw_data_trace = go.Scatter(
                    x=df.index,
                    y=df.iloc[:,0].values,
                    mode='markers+lines',
                    # marker=go.Marker(color='rgb(255, 127, 14)'),
                    name='Raw Data'
                    )
    


    linear_fit_trace = go.Scatter(
        x=df.index,
        y=line,
        mode="markers+lines",
        name="Linear Fit"
    )
    data = [
        raw_data_trace,
        linear_fit_trace

    ]
    layout = {
        'title': f'Data Visualization <br><b>Linear Fit :</b>y={round(slope,3)}x+{round(intercept,3)},r_value:{round(r_value,3)}',
        "autosize": False,
        # "margin": dict(t=10, b=10, l=40, r=0, pad=10),
        "xaxis": {"title": "Time (ds)"},
        "yaxis":{"title":"Grip Strength (g)"}
    }
    return data,layout