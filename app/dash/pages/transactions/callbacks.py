from datetime import datetime
from dash import callback, Input, Output, State, no_update
from flask import session
from .transactions_controller import (
    prepare_transaction_for_insertion,
    insert_transaction,
)


def initialize_callbacks():
    @callback(
        Output("input_date", "value"),
        Output("input_transaction_name", "value"),
        Output("selector_transaction_category", "value"),
        Output("input_transaction_value", "value"),
        Output("selector_transaction_frequency", "value"),
        Output("input_transaction_description", "value"),
        Output("switch_transaction_type", "checked"),
        Output("input_transaction_name", "error"),
        Output("input_transaction_value", "error"),
        Output("transaction_insert_confirmation", "children"),
        Input("button_add_new", "n_clicks"),
        State("input_date", "value"),
        State("switch_transaction_type", "checked"),
        State("input_transaction_name", "value"),
        State("selector_transaction_category", "value"),
        State("input_transaction_value", "value"),
        State("selector_transaction_frequency", "value"),
        State("input_transaction_description", "value"),
        prevent_initial_call=True,
    )
    def insert_new_transaction(
        n_clicks, date, transaction_type, name, category, value, frequency, description
    ):
        """This callback verifies if the user has filled all the required fields (name and value), if yes then inserts a new transaction into the database and clear the input fields."""
        if n_clicks:
            if (name is None or name == "") and (value == 0):
                return (
                    no_update,
                    no_update,
                    no_update,
                    no_update,
                    no_update,
                    no_update,
                    no_update,
                    True,
                    True,
                    no_update,
                )
            if name is None or name == "":
                return (
                    no_update,
                    no_update,
                    no_update,
                    no_update,
                    no_update,
                    no_update,
                    no_update,
                    True,
                    False,
                    no_update,
                )
            if value == 0:
                return (
                    no_update,
                    no_update,
                    no_update,
                    no_update,
                    no_update,
                    no_update,
                    no_update,
                    False,
                    True,
                    no_update,
                )
            user_id = session.get("user_id")
            new_transaction = prepare_transaction_for_insertion(
                date,
                transaction_type,
                name,
                category,
                value,
                frequency,
                description,
                user_id,
            )
            insert_transaction(new_transaction)
            return (
                datetime.now().date(),
                "",
                "others",
                0,
                "one-time",
                "",
                False,
                False,
                False,
                "Adicionada com sucesso!",
            )
        return no_update

    @callback(
        Output("selector_transaction_frequency", "style"),
        Output("selector_transaction_frequency", "value", allow_duplicate=True),
        Input("switch_recurrence", "checked"),
        prevent_initial_call=True,
    )
    def show_transaction_frequency_input(checked):
        if checked:
            return {"display": "block"}, "monthly"
        return {"display": "none"}, "one-time"
