import pandas as pd
import plotly.graph_objs as go
import numpy as np
from scipy import stats
from scipy.optimize import curve_fit
import base64
import io


def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(",")

    decoded = base64.b64decode(content_string)
    try:
        if "csv" in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode("utf-8")),
                # header=None,
                # names=["Time", "Grip Strength"],
            )
            df.set_index("Time", inplace=True)
            df.dropna(axis=1,inplace=True)
            return df

    except Exception as e:
        print(e)


def linear_fit(xi, y):
    """
    Uses scipy.stats to run OLS
    """
    # Generated linear fit
    slope, intercept, r_value, p_value, std_err = stats.linregress(xi, y)
    line = slope * xi + intercept
    return slope, intercept, r_value, p_value, std_err, line


def polynomial_fit(xi, y, degree):
    """
    Uses numpy.polyfit to calculate a Polynomial fit for a provided degree.
    Returns a numpy.poly1id object
    """
    z = np.polyfit(xi, y, degree)
    f = np.poly1d(z)
    return f


def exponenial_func(x, a, b, c):
    return a * np.exp(-b * x) + c


def setup_graph(df):
    """
    Sets up a Graph of a Timeseries DataFrame.
    Returns data and layout
    """
    # Linear Fit
    slope, intercept, r_value, p_value, std_err, line = linear_fit(
        df.index, df.iloc[:, 0].values
    )
    # Quadratic Fit
    f_quadratic = polynomial_fit(df.index, df.iloc[:, 0].values, 2)
    # Cubic Fit
    f_cubic = polynomial_fit(df.index, df.iloc[:, 0].values, 3)
    # Exponentional Fit
    popt, pcov = curve_fit(
        exponenial_func, df.index, df.iloc[:, 0].values, p0=(1, 1e-6, 1)
    )
    # Add a Trace of the Raw Data
    raw_data_trace = go.Scatter(
        x=df.index,
        y=df.iloc[:, 0].values,
        mode="markers+lines",
        # marker=go.Marker(color='rgb(255, 127, 14)'),
        name="Raw Data",
    )

    linear_fit_trace = go.Scatter(
        x=df.index, y=line, mode="markers+lines", name="Linear Fit"
    )

    quadratic_fit_trace = go.Scatter(
        x=df.index, y=f_quadratic(df.index), mode="markers+lines", name="Quadratic Fit"
    )

    cubic_fit_trace = go.Scatter(
        x=df.index, y=f_cubic(df.index), mode="markers+lines", name="Cubic Fit"
    )

    exponential_fit_trace = go.Scatter(
        x=df.index,
        y=exponenial_func(df.index, *popt),
        mode="markers+lines",
        name="Exponential Fit",
    )
    data = [
        raw_data_trace,
        linear_fit_trace,
        quadratic_fit_trace,
        cubic_fit_trace,
        exponential_fit_trace,
    ]
    layout = {
        "title": f"""Data Visualization 
        <br>
        <b>Linear Fit:</b> y={round(slope,5)}x+{round(intercept,5)},r_value:{round(r_value,3)}
        <br>
        <b> Quadratic Fit:</b> y = {round(f_quadratic[0],3)}x^2+{round(f_quadratic[1],3)}x+{round(f_quadratic[2],3)}
        """,
        "autosize": False,
        # "margin": dict(t=10, b=10, l=40, r=0, pad=10),
        "xaxis": {"title": "Time (ds)"},
        "yaxis": {"title": "Grip Strength (g)"},
    }
    return data, layout
