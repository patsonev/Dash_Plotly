import dash
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt

app = dash.Dash()

app.layout = html.Div([
    dcc.RadioItems(
        options=[
            {"label": "Pleven", "value": "PL"},
            {"label": "Plovdiv", "value": "PLO"},
            {"label": "Sofia", "value": "SO"}
        ],
        value="SO"
    ),

    html.Button("Submit", id="submit_form"),

    html.Br(),
    html.Br(),

    dcc.DatePickerSingle(
        id="dt-pick-single",
        date=dt(2020, 6, 22)
    ),

    html.Br(),
    html.Br(),

    dcc.DatePickerRange(
        id="dt-pick-range1",
        start_date=dt(2020, 2, 20),
        end_date=dt(2020, 6, 12)
    ),

    html.Br(),
    html.Br(),

    dcc.DatePickerRange(
        id="dt-pick-range2",
        start_date=dt(2020, 2, 20),
        end_date_placeholder_text="Select the date"
    ),

    html.Br(),
    html.Br(),

    dcc.DatePickerRange(
        id="dt-pick-range3",
        start_date_placeholder_text="Select start date",
        end_date_placeholder_text="Select end date"
    )
])

if __name__ == "__main__":
    app.run_server(port=5050)
