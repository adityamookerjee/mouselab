import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

PLOTLY_LOGO = "https://www.freelogodesign.org/file/app/client/thumb/8b2e9def-4220-49c5-b7aa-eac3fa029999_200x200.png"

NAVBAR = dbc.Navbar(
    children=[
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                    dbc.Col(dbc.NavbarBrand("MouseLab", className="ml-2")),
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

UPLOAD_PLOT = [
    dbc.CardHeader(html.H5("Data Visualization")),
    dbc.CardBody(
        [
            dcc.Loading(
                id="loading-banks-hist",
                children=[html.Div(id="data-analysis-div")],
                type="default",
            )
        ]
    ),
    dcc.Store(id="data-store", storage_type="local"),
]

DATA_TABLE = [
    dbc.CardHeader(html.H5("Data Table")),
    dbc.CardBody([html.Div(id="data-table-div")]),
]

STATS = [
    dbc.CardHeader(html.H5("Statistics")),
    dbc.CardBody([html.Div(id="stats-table-div")]),
]

LEFT_COLUMN = dbc.Jumbotron(
    [
        html.H4(children="Upload and Configure Experiment", className="display-5"),
        html.Hr(className="my-2"),
        html.Label("Upload Data", className="lead"),
        html.P(
            "Important! : In the .csv, the first column must be 'Time' and the second must be the 'Reading' ",
            style={"fontSize": 10, "font-weight": "lighter"},
        ),
        UPLOAD_COMPONENT,
    ]
)

BODY = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(LEFT_COLUMN, md=4, align="center"),
                dbc.Col(dbc.Card(UPLOAD_PLOT), md=8),
            ]
        ),
        dbc.Row(
            [dbc.Col(dbc.Card(DATA_TABLE), md=4), dbc.Col(dbc.Card(STATS), md=8)],
            style={"marginTop": 50},
        ),
        # dbc.Card(WORDCLOUD_PLOTS),
        # dbc.Row([dbc.Col([dbc.Card(LDA_PLOTS)])], style={"marginTop": 50}),
    ],
    className="mt-12",
)
