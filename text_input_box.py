import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    html.Label("This is simple input box: "),
    dcc.Input(
        placeholder="Type your text here",
        type="text",
        value="",
    ),

    html.Br(),
    html.Br(),

    html.Label("This is simple text area: "),
    dcc.Textarea(
        placeholder="Type your text here",
        value="",
        style={"width": "30%"}
        )

])

if __name__ == "__main__":
    app.run_server(port=5050)