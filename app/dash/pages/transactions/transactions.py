import dash
from dash import html
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from .components.input_transaction import render_input_new_transaction_card
from .components.bank_info_input import render_bank_info_input_card
from .components.table import render_table_card
from .callbacks import initialize_callbacks

dash.register_page(__name__, path="/")

initialize_callbacks()


def layout():
    return dbc.Container(
        id="transactions_page_container",
        children=[
            dbc.Row([html.Br()]),
            dbc.Row(
                [
                    dmc.Group(
                        [
                            render_input_new_transaction_card(),
                            render_bank_info_input_card(),
                        ]
                    ),
                ]
            ),
            html.Br(),
            dbc.Row([render_table_card()]),
        ],
        style={"paddingBottom": "3vh"},
    )
