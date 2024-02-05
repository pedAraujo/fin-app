from dash import Dash
from app.auth.routes import login_required
import dash_bootstrap_components as dbc
import logging

url_base_pathname = "/finapp/"
app_title = "Fin App - Controle de finanças"
logger = logging.getLogger(__name__)


def init_dash_app(flask_server):
    from app.dash.components.main_layout import create_main_layout
    from app.dash.components.callbacks import register_callbacks

    # Meta tag required for viewport responsiveness
    meta_viewport = {
        "name": "viewport",
        "content": "width=device-width, initial-scale=1, shrink-to-fit=no",
    }

    app = Dash(
        __name__,
        server=flask_server,
        url_base_pathname=url_base_pathname,
        assets_folder=f"{flask_server.config.root_path}/static",
        meta_tags=[meta_viewport],
        title=app_title,
        use_pages=True,
        external_stylesheets=[dbc.themes.BOOTSTRAP],
    )
    app.enable_dev_tools(
        dev_tools_ui=True,
        dev_tools_serve_dev_bundles=True,
        dev_tools_hot_reload=True,
    )

    app.title = app_title
    app.layout = create_main_layout(app)
    register_callbacks(app)

    _protect_dash_views(app)


def _protect_dash_views(dash_app):
    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function]
            )
