from dash import Input, Output
from flask import session


def register_callbacks(app):
    # callback to update the username in the navbar when page loads
    @app.callback(
        Output("username", "children"),
        Input("url", "pathname"),
    )
    def update_username(_):
        return session.get("username", "")
