from datetime import datetime
from app.dash import logger
from dash import callback, Input, Output, State, no_update
from flask import session
from .transactions_controller import (
    get_transactions_by_user,
    insert_transaction,
)


def initialize_callbacks():
    @callback(
        Output("transactions_table", "rowData", allow_duplicate=True),
        Output("input_date", "value"),
        Output("input_transaction_name", "value"),
        Output("selector_transaction_category", "value"),
        Output("input_transaction_value", "value"),
        Output("selector_transaction_frequency", "value"),
        Output("input_transaction_description", "value"),
        Output("switch_transaction_type", "checked"),
        Output("input_transaction_name", "error"),
        Output("input_transaction_value", "error"),
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
                    no_update,
                    True,
                    True,
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
                    no_update,
                    True,
                    False,
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
                    no_update,
                    False,
                    True,
                )
            user_id = session.get("user_id")
            if insert_transaction(
                date=date,
                transaction_type=transaction_type,
                name=name,
                category=category,
                value=value,
                frequency=frequency,
                description=description,
                user_id=user_id,
                created_at=datetime.now(),
            ):
                transactions = (
                    get_transactions_by_user(user_id)
                    .drop("_id", axis=1)
                    .to_dict("records")
                )
                logger.info("New transaction inserted")
                return (
                    transactions,
                    datetime.now(),
                    "",
                    "others",
                    0,
                    "one-time",
                    "",
                    False,
                    False,
                    False,
                )
            return (
                no_update,
                no_update,
                no_update,
                no_update,
                no_update,
                no_update,
                no_update,
                no_update,
                no_update,
                False,
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

    @callback(
        Output("transactions_table", "rowData"),
        Input("transactions_page_container", "children"),
    )
    def load_transactions_on_page_load(_):
        user_id = session.get("user_id")
        transactions = get_transactions_by_user(user_id).drop("_id", axis=1)
        return transactions.to_dict("records")
