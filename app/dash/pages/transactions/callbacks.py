from dash import callback, Input, Output, State, no_update
from flask import session
from app.mongo import get_user_id_from_username


def initialize_callbacks():
    # callback to add transaction to the database and table
    # TODO - add Table outputs to this callback
    @callback(
        Output("hello", "children"),
        Input("button_add_new", "n_clicks"),
        State("input_date", "value"),
        State("switch_income_expense", "checked"),
        State("input_transaction_name", "value"),
        State("input_transaction_value", "value"),
        State("selector_transaction_frequency", "value"),
        State("input_transaction_description", "value"),
    )
    def say_hello(n_clicks, date, income_expense, name, value, frequency, description):
        transaction_info = {
            "Data": date,
            "Movimentacao": income_expense,
            "name": name,
            "value": value,
            "frequency": frequency,
            "description": description,
        }
        user_id = get_user_id_from_username(session["username"])
        if n_clicks:
            print(transaction_info)
            print(user_id)
            return "printed"
        # TODO - add transaction to the database - figure out how to fit to the schema
        return no_update

    # callback to hide transaction frequency if switch is off
    @callback(
        Output("selector_transaction_frequency", "style"),
        Output("selector_transaction_frequency", "value"),
        Input("switch_recurrence", "checked"),
        prevent_initial_call=True,
    )
    def hide_transaction_frequency(checked):
        if checked:
            return {"display": "block"}, "monthly"
        return {"display": "none"}, "once"
