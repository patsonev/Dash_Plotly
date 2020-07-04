import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    html.Label("This is a simple slider."),
    dcc.Slider(
        min=1,
        max=10,
        value=3,
        step=0.5,
        marks={i: i for i in range(10)}
    ),

    html.Br(),
    html.Br(),

    html.Label("Range slider"),
    dcc.RangeSlider(
        min=1,
        max=10,
        step=0.5,
        value=[3, 6],
        marks={i: i for i in range(10)}
    )
])

if __name__ == "__main__":
    app.run_server(port=5050)
