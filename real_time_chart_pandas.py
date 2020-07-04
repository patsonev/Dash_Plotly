import dash
import dash_core_components as dcc
import plotly.graph_objects as go
import dash_html_components as html
import pandas as pd
import numpy as np

app = dash.Dash()

order = pd.read_excel("asd.xls")

app.layout = html.Div([

    dcc.Graph(
        id="scatter_plot",
        figure={
            "data": [
                go.Scatter(
                    x=order.Sales,
                    y=order.Profit,
                    mode='markers'
                )
            ],
            "layout": go.Layout(
                title="Scatter plot of random points",
                xaxis = {"title": "Sales"},
                yaxis = {"title": "Profit"},
                # hovermode="closest"
            )
        }
    )
])

if __name__ == "__main__":
    app.run_server(port=5050)
