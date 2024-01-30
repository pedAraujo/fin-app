from dash import html
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from ..callbacks import initialize_callbacks

initialize_callbacks()

input_date = dmc.TextInput(label="Data", type="date", id="input_date")

switch_income_expense = dmc.Switch(
    id="switch_income_expense",
    offLabel=DashIconify(icon="ic:outline-money-off", width=20),
    onLabel=DashIconify(icon="ic:outline-attach-money", width=20),
    size="lg",
    color="teal",
    checked=False,
    styles={"track": {"background-color": "#fa5252", "color": "white"}},
)

input_transaction_name = dmc.TextInput(
    label="Título",
    type="text",
    id="input_transaction_name",
)

input_transaction_value = dmc.NumberInput(
    id="input_transaction_value",
    label="Valor",
    min=0,
    precision=2,
    icon=DashIconify(icon="tabler:currency-real"),
)

selector_transaction_category = dmc.Select(
    id="selector_transaction_category",
    label="Categoria",
    data=[
        {"label": "Bares", "value": "bars"},
        {"label": "Compras", "value": "shopping"},
        {"label": "Contas", "value": "bills"},
        {"label": "Entretenimento", "value": "entertainment"},
        {"label": "Impostos e Taxas", "value": "taxes"},
        {"label": "Educação", "value": "education"},
        {"label": "Mercado", "value": "market"},
        {"label": "Outros", "value": "others"},
        {"label": "Presentes", "value": "gifts"},
        {"label": "Restaurante", "value": "restaurant"},
        {"label": "Roupas", "value": "clothes"},
        {"label": "Saúde e Fitness", "value": "health and fitness"},
        {"label": "Serviços e Assinaturas", "value": "services and subscriptions"},
        {"label": "Transporte", "value": "transport"},
        {"label": "Viagem", "value": "travel"},
    ],
)

switch_recurrence = dmc.Switch(
    id="switch_recurrence",
    label="Recorrente",
    size="sm",
    checked=False,
)

selector_transaction_frequency = dmc.Select(
    id="selector_transaction_frequency",
    label="Recorrência",
    value="once",
    data=[
        {"label": "Semanal", "value": "weekly"},
        {"label": "Mensal", "value": "monthly"},
        {"label": "Anual", "value": "yearly"},
    ],
    style={"display": "none"},
)

input_transaction_description = dmc.Textarea(
    id="input_transaction_description",
    label="Descrição",
    placeholder="Descrição da transação",
    style={"width": "100%"},
    autosize=True,
    minRows=2,
    maxRows=4,
)

button_add_new = dmc.Button(
    "Adicionar",
    id="button_add_new",
    color="teal",
    size="sm",
)


def render_input_new_transaction_card():
    return dmc.Card(
        [
            dmc.CardSection(
                [
                    dmc.Group(
                        [
                            switch_income_expense,
                            dmc.Text("Adicionar transação"),
                            dmc.Space(),
                        ],
                        position="center",
                        align="center",
                        grow="True",
                    ),
                ],
                withBorder=True,
                inheritPadding=True,
                py="xs",
            ),
            dmc.CardSection(
                [
                    dmc.Group(
                        [
                            input_date,
                            input_transaction_name,
                        ]
                    ),
                    dmc.Group(
                        [
                            input_transaction_value,
                            html.Br(),
                            switch_recurrence,
                        ]
                    ),
                    html.Br(),
                    selector_transaction_frequency,
                    html.Br(),
                    input_transaction_description,
                ],
                inheritPadding=True,
                py="xs",
            ),
            dmc.CardSection(
                [button_add_new],
                style={"display": "flex", "justify-content": "center"},
                inheritPadding=True,
                py="xs",
            ),
        ],
        withBorder=True,
        shadow="sm",
        radius="md",
    )