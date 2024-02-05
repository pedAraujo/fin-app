import dash_ag_grid as dag
import dash_mantine_components as dmc


column_defs = [
    {
        "field": "date",
        "headerName": "Data",
        "valueGetter": {"function": "d3.timeParse('%Y-%m-%d')(params.data.date)"},
        "valueFormatter": {
            "function": "d3.timeFormat('%d/%m/%Y')(d3.timeParse('%Y-%m-%d')(params.data.date))"
        },
    },
    {"field": "name", "headerName": "Nome"},
    {"field": "category", "headerName": "Categoria"},
    {
        "field": "value",
        "headerName": "Valor",
    },
    {"field": "frequency", "headerName": "Frequência"},
    {"field": "description", "headerName": "Descrição"},
    {"field": "type", "headerName": "Tipo"},
    {
        "field": "created_at",
        "hide": True,
        "sort": "desc",
    },
]


transactions_table = dag.AgGrid(
    id="transactions_table",
    columnDefs=column_defs,
    defaultColDef={
        "resizable": True,
        "sortable": True,
        "filter": True,
    },
    dashGridOptions={
        "rowSelection": "multiple",
        "sortingOrder": ["desc", "asc", None],
        "loadingOverlayComponent": "CustomLoadingOverlay",
        "loadingOverlayComponentParams": {
            "loadingMessage": "Carregando...",
        },
        "pagination": True,
        "dataTypeDefinitions": {"function": "dataTypeDefinitions"},
    },
)


def render_table_card():
    return dmc.Paper(
        [dmc.Text("TRANSAÇÕES"), transactions_table],
        withBorder=True,
        shadow="sm",
        radius="md",
    )
