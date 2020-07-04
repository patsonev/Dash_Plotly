import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()

app.layout = html.Div([
    dcc.RadioItems(
        id="change_color",
        options=[
            {"label": "red", "value": "red"},
            {"label": "green", "value": "green"}
        ],
        value="red",
        style={"background-color": "red"}
    )
])


@app.callback(
    dash.dependencies.Output("change_color", "style"),
    [dash.dependencies.Input("change_color", "value")]
)
def changing_the_color(color):
    return {"background-color": color}


if __name__ == "__main__":
    app.run_server(port=5050)
