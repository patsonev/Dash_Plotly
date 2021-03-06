import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

colors = {
    "text": "red",
    "plot_color": "blue",
    "paper_color": "green"
}

app.layout = html.Div([
    html.H1(children="Hello dash plotly",
            style={
                "textAlign": "center",
                "color": colors["text"]
            }
            ),
    html.Div(children="If this framework is perfect for my projects I will be so excited!",
             style={
                 "textAlign": "center",
                 "color": colors["text"]
             }
             ),

    dcc.Graph(
        id="simple-graph",
        figure={
            "data": [
                {"x": [4, 6, 8], "y": [12, 16, 18], "type": "bar", "name": "First Chart"},
                {"x": [5, 7, 9], "y": [13, 9, 6], "type": "bar", "name": "Second Chart"},
                {"x": [4, 6, 8], "y": [1, 10, 8], "type": "bar", "name": "Third Chart"}
            ],
            "layout": {
                "plot_bgcolor": colors["plot_color"],
                "paper_bgcolor": colors["paper_color"],
                "font": {
                    "color": colors["text"]
                },
                "title": "Data visualisation with Bar Chart"
            }
        }
    )
])

if __name__ == "__main__":
    app.run_server(port=4050)
