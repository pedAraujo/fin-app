import dash
from dash import html
from dash import dcc
from .navbar import create_navbar

NAVBAR = create_navbar()
URL = dcc.Location(id="url", refresh=True)


def create_main_layout(dash_app: dash) -> html.Div:
    dash_app.layout = html.Div(
        children=[
            URL,
            html.Div(
                [NAVBAR, dash.page_container],
                className="main-body",
            ),
        ],
    )
    return dash_app.layout
