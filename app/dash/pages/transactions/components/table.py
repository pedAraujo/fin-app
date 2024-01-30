import dash_ag_grid as dag
import pandas as pd
import dash_mantine_components as dmc

# simple df to test
df = pd.DataFrame(
    {
        "direction": ["north", "south", "east", "west"],
        "strength": [1, 2, 3, 4],
        "frequency": [5, 6, 7, 8],
    }
)

columnDefs = [
    {"field": "direction"},
    {"field": "strength"},
    {"field": "frequency"},
]

transactions_table = dag.AgGrid(
    id="transactions_table",
    rowData=df.to_dict("records"),
    columnDefs=columnDefs,
)


def render_table():
    return dmc.Paper(
        [transactions_table],
        withBorder=True,
        shadow="sm",
        radius="md",
    )
