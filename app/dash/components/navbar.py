import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

from dash import html, dcc

logout_button = dcc.Link(
    dmc.Button(
        children=[
            "Sair",
            html.I(className="navbutton-icon fa-solid fa-arrow-right-from-bracket"),
        ],
        color="red",
    ),
    href="/auth/logout",
    refresh=True,
)


title = dmc.Text("Fin App", className="navbar-title")

username = dmc.Text("", size="sm", id="username")


def create_navbar() -> dbc.Navbar:
    return dbc.Navbar(
        children=[
            dmc.Grid(
                [
                    dmc.Col(
                        title, span=6, style={"textAlign": "Left", "justify": "center"}
                    ),
                    dmc.Col(
                        [
                            dmc.Group(
                                [
                                    dmc.Text("Olá, ", size="sm"),
                                    username,
                                    logout_button,
                                ],
                                position="right",
                                align="center",
                            ),
                        ],
                        span=6,
                    ),
                ],
                align="center",
                justify="space-around",
                grow=True,
                style={"width": "100%", "paddingInline": "10vw"},
            ),
        ],
        color="lightGray",
    )
