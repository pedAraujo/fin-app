import dash
from dash import html
import dash_bootstrap_components as dbc

# from .callbacks import initialize_callbacks
from .components.input_transaction import render_input_new_transaction_card
from .components.table import render_table

dash.register_page(__name__, path="/")


def layout():
    return dbc.Container(
        [
            dbc.Row([html.Br()]),
            dbc.Row(
                [
                    render_input_new_transaction_card(),
                ]
            ),
            dbc.Row([html.Br(), render_table()]),
        ]
    )
