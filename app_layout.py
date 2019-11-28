import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

NAVBAR = dbc.Navbar(
    children=[
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                    dbc.Col(dbc.NavbarBrand("Mouse Lab", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            ),
            href="https://plot.ly",
        )
    ],
    color="dark",
    dark=True,
    sticky="top",
)

UPLOAD_COMPONENT = html.Div(
    [
        dcc.Upload(
            id="upload-data",
            children=html.Div(["Drag and Drop or ", html.A("Select Files")]),
            style={
                "width": "100%",
                "height": "60px",
                "lineHeight": "60px",
                "borderWidth": "1px",
                "borderStyle": "dashed",
                "borderRadius": "5px",
                "textAlign": "center",
                "margin": "10px",
            },
            multiple=False,
        )
    ]
)

TOP_BANKS_PLOT = [
    dbc.CardHeader(html.H5("Data Visualization")),
    dbc.CardBody(
        [
            dcc.Loading(
                id="loading-banks-hist",
                children=[dcc.Graph(id="data-plot")],
                type="default",
            )
        ]
    ),
]

LEFT_COLUMN = dbc.Jumbotron(
    [
        html.H4(children="Upload and Configure Experiment", className="display-5"),
        html.Hr(className="my-2"),
        html.Label("Upload Data", className="lead"),
        html.P(
            "(<Enter File information here>)",
            style={"fontSize": 10, "font-weight": "lighter"},
        ),
        UPLOAD_COMPONENT,
        # dcc.Slider(
        #     id="n-selection-slider",
        #     min=1,
        #     max=100,
        #     step=1,
        #     marks={
        #         0: "0%",
        #         10: "",
        #         20: "20%",
        #         30: "",
        #         40: "40%",
        #         50: "",
        #         60: "60%",
        #         70: "",
        #         80: "80%",
        #         90: "",
        #         100: "100%",
        #     },
        #     value=20,
        # ),
        # html.Label("Select a bank", style={"marginTop": 50}, className="lead"),
        # html.P(
        #     "(You can use the dropdown or click the barchart on the right)",
        #     style={"fontSize": 10, "font-weight": "lighter"},
        # ),
        # dcc.Dropdown(
        #     id="bank-drop", clearable=False, style={"marginBottom": 50, "font-size": 12}
        # ),
        # html.Label("Select time frame", className="lead"),
        # html.Div(dcc.RangeSlider(id="time-window-slider"), style={"marginBottom": 50}),
        # html.P(
        #     "(You can define the time frame down to month granularity)",
        #     style={"fontSize": 10, "font-weight": "lighter"},
        # ),
    ]
)

BODY = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(LEFT_COLUMN, md=4, align="center"),
                dbc.Col(dbc.Card(TOP_BANKS_PLOT), md=8),
            ],
            style={"marginTop": 30},
        ),
        # dbc.Card(WORDCLOUD_PLOTS),
        # dbc.Row([dbc.Col([dbc.Card(LDA_PLOTS)])], style={"marginTop": 50}),
    ],
    className="mt-12",
)
