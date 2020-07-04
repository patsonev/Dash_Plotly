import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    html.Label("Single choose a city"),
    dcc.Dropdown(
        id="first-dropdown",
        options=[
            {"label": "Pleven", "value": "PL"},
            {"label": "Plovdiv", "value": "PLO"},
            {"label": "Sofia", "value": "SO"}
        ],
        value="PL",
    ),

    html.Label("Multiple selection"),
    dcc.Dropdown(
        id="second-dropdown",
        options=[
            {"label": "Pleven", "value": "PL"},
            {"label": "Plovdiv", "value": "PLO"},
            {"label": "Sofia", "value": "SO"}
        ],
        value="PL",
        multi=True
    ),

    html.Label("Dropdown with placeholder"),
    dcc.Dropdown(
        id="third-dropdown",
        options=[
            {"label": "Pleven", "value": "PL"},
            {"label": "Plovdiv", "value": "PLO"},
            {"label": "Sofia", "value": "SO"}
        ],
        placeholder="Select your city"
    ),

    html.Label("Disable dropdown menu"),
    dcc.Dropdown(
        id="fourth-dropdown",
        options=[
            {"label": "Pleven", "value": "PL"},
            {"label": "Plovdiv", "value": "PLO"},
            {"label": "Sofia", "value": "SO"}
        ],
        disabled=True
    ),

    html.Label("Disable only one choice from menu"),
    dcc.Dropdown(
        id="fifth-dropdown",
        options=[
            {"label": "Pleven", "value": "PL"},
            {"label": "Plovdiv", "value": "PLO"},
            {"label": "Sofia", "value": "SO", "disabled": True}
        ],
    )
])

if __name__ == "__main__":
    app.run_server(port=5050)
