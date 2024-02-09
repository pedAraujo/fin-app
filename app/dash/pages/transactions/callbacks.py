from datetime import datetime
from app.dash import logger
from dash import callback, Input, Output, State, no_update
from flask import session
from .transactions_controller import (
    get_transactions_by_user,
    get_user_by_id,
    insert_transaction,
    update_user_balance_info,
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
        Output("selector_transaction_frequency", "style", allow_duplicate=True),
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

    @callback(
        Output("input_balance", "value"),
        Output("input_credit_card_invoice", "value"),
        Input("transactions_page_container", "children"),
    )
    def load_user_balance_and_invoice(_):
        user_id = session.get("user_id")
        user = get_user_by_id(user_id)
        return user["account_balance"]["balance"], user["account_balance"]["invoice"]

    @callback(
        Output("resulting_balance_value", "children"),
        Input("input_balance", "value"),
        Input("input_credit_card_invoice", "value"),
        prevent_initial_call=True,
    )
    def calculate_resulting_balance(balance, invoice):
        balance = float(balance)
        invoice = float(invoice)
        total_balance = balance - invoice
        return f"R$ {total_balance:.2f}" if balance and invoice else "R$ 0,00"

    # update user balance and invoice on db
    @callback(
        Output("input_balance", "value", allow_duplicate=True),
        Output("input_credit_card_invoice", "value", allow_duplicate=True),
        Input("input_balance", "value"),
        Input("input_credit_card_invoice", "value"),
        prevent_initial_call=True,
    )
    def update_user_balance_and_invoice(balance, invoice):
        if balance != 0 and invoice != 0:
            user_id = session.get("user_id")
            balance_info = {"balance": float(balance), "invoice": float(invoice)}
            if update_user_balance_info(user_id, balance_info):
                return balance, invoice
        return no_update, no_update
