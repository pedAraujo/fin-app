import dash_mantine_components as dmc
import dash_bootstrap_components as dbc

text_style = {
    "fontFamily": "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji",
    "lineHeight": "1.5",
    "fontSize": "14px",
    "fontWeight": 500,
    "color": "rgb(33, 37, 41)",
}

input_balance = dbc.Input(
    id="input_balance",
    type="number",
    value=0,
    min=0,
    required=True,
    debounce=True,
    style={"width": "50%"},
)


input_credit_card_invoice = dbc.Input(
    id="input_credit_card_invoice",
    type="number",
    value=0,
    min=0,
    required=True,
    debounce=True,
    style={"width": "50%"},
)

resulting_balance_value = dmc.Text(
    id="resulting_balance_value",
    children="R$ 0,00",
)

resulting_balance = dmc.Paper(
    id="resulting_balance",
    children=[
        dmc.Stack(
            [
                dmc.Text("Saldo após pagamento da fatura", style=text_style),
                resulting_balance_value,
            ],
            align="center",
        ),
    ],
)


def render_bank_info_input_card():
    return dmc.Card(
        [
            dmc.CardSection(
                [
                    dmc.Group(
                        [
                            dmc.Text(
                                "INFORMAÇÕES DA SUA CONTA",
                            ),
                        ],
                        position="center",
                        align="center",
                        spacing=30,
                    ),
                ],
                withBorder=True,
                inheritPadding=True,
                py="xs",
            ),
            dmc.CardSection(
                [],
                inheritPadding=True,
                py="xs",
            ),
            dmc.CardSection(
                [
                    dmc.Stack(
                        [
                            dmc.Group(
                                [
                                    dmc.Text(
                                        "Saldo disponível",
                                        style=text_style,
                                    ),
                                    dmc.Text("R$", style=text_style),
                                    input_balance,
                                ],
                                position="right",
                                spacing="xs",
                            ),
                            dmc.Group(
                                [
                                    dmc.Text("Fatura", style=text_style),
                                    dmc.Text("R$", style=text_style),
                                    input_credit_card_invoice,
                                ],
                                position="right",
                                spacing="xs",
                            ),
                        ]
                    ),
                ],
                inheritPadding=True,
                py="xs",
            ),
            resulting_balance,
        ],
        withBorder=True,
        shadow="sm",
        radius="md",
        style={"maxWidth": "100%"},
    )
