from dash import Dash
from app.auth.routes import login_required

url_base_pathname = "/finapp/"
assets_folder = "static"
app_title = "Fin App - Controle de finanças"


def init_dash_app(flask_server):
    from app.dash.layout import layout
    from app.dash.callbacks import register_callbacks

    # Meta tag required for viewport responsiveness
    meta_viewport = {
        "name": "viewport",
        "content": "width=device-width, initial-scale=1, shrink-to-fit=no",
    }

    app = Dash(
        __name__,
        server=flask_server,
        url_base_pathname=url_base_pathname,
        assets_folder=assets_folder,
        meta_tags=[meta_viewport],
    )

    app.title = app_title
    app.layout = layout
    register_callbacks(app)

    _protect_dash_views(app)


def _protect_dash_views(dash_app):
    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function]
            )
