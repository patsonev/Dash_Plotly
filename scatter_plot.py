import dash
import dash_core_components as dcc
import plotly.graph_objects as go
import dash_html_components as html
import numpy as np

app = dash.Dash()

np.random.seed(50)
x_rand = np.random.randint(1, 61, 60)
y_rand = np.random.randint(1, 61, 60)

app.layout = html.Div([

    dcc.Graph(
        id="scatter_plot",
        figure={
            "data": [
                go.Scatter(
                    x=x_rand,
                    y=y_rand,
                    mode='lines'
                )
            ],
            "layout": go.Layout(
                title="Scatter plot of random points",
                xaxis = {"title": "Random x values"},
                yaxis = {"title": "Random y values"}
            )
        }
    )
])

if __name__ == "__main__":
    app.run_server(port=5050)
