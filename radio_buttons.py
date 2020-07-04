import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    dcc.RadioItems(
        options=[
            {"label": "Pleven", "value": "PL"},
            {"label": "Plovdiv", "value": "PLO"},
            {"label": "Sofia", "value": "SO"}
        ],
        value="SO"
    )
])

if __name__ == "__main__":
    app.run_server(port=5050)
