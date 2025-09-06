import pandas as pd
from dash import Dash, dcc, html, dash_table, Input, Output
import plotly.express as px
from pathlib import Path

# Path to the CSV file
DATA_PATH = Path("data/animals.csv")

# Load dataset
df = pd.read_csv(DATA_PATH)

# Initialize Dash app
app = Dash(__name__)
server = app.server  # for deployment if needed

# Layout
app.layout = html.Div([
    html.H2("Grazioso Salvare – Animal Rescue Dashboard"),
    html.P("Filter by rescue type to explore animals, view table data, and breed distribution."),

    dcc.Dropdown(
        id="rescue-type",
        options=[{"label": x, "value": x} for x in sorted(df["rescue_type"].unique())],
        value=None,
        placeholder="Filter by rescue type",
        clearable=True,
        style={"maxWidth": 420}
    ),

    dash_table.DataTable(
        id="table",
        columns=[{"name": c, "id": c} for c in ["id", "rescue_type", "breed", "age"]],
        page_size=5,
        style_table={"maxWidth": 700},
        style_cell={"textAlign": "left"}
    ),

    dcc.Graph(id="breed-chart"),
])

# Callbacks
@app.callback(
    Output("table", "data"),
    Output("breed-chart", "figure"),
    Input("rescue-type", "value")
)
def update_dashboard(rescue_type):
    filt = df[df["rescue_type"].eq(rescue_type)] if rescue_type else df
    fig = px.histogram(filt, x="breed", title="Breed Distribution", text_auto=True)
    fig.update_layout(margin=dict(l=20, r=20, t=40, b=20))
    return filt.to_dict("records"), fig

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
