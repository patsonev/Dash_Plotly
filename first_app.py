import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

all_options = {
    "America": ["New York City", "San Francisco", "Cincinnati"],
    "Canada": ["Montreal", "Toronto", "Ottawa"],
    "All": ["New York City", "San Francisco", "Cincinnati", "Montreal", "Toronto", "Ottawa"]
}

city_data = {
    'San Francisco': {'x': [1, 2, 3], 'y': [4, 1, 2]},
    'Montreal': {'x': [1, 2, 3], 'y': [2, 4, 5]},
    'New York City': {'x': [1, 2, 3], 'y': [2, 2, 7]},
    'Cincinnati': {'x': [1, 2, 3], 'y': [1, 0, 2]},
    'Toronto': {'x': [1, 2, 3], 'y': [4, 7, 3]},
    'Ottawa': {'x': [1, 2, 3], 'y': [2, 3, 3]}
}

app.layout = html.Div(
    html.Div([
        html.Div([
            html.H1(children="Hello World"),
            html.Div(children="""
            Dash: A web application framework for Python.
            """)
        ], style={"margin-left": "10%"}),

        html.Div([
            html.Div([
                html.P("Choose City: "),
                dcc.Checklist(
                    id="Cities",
                    options=[
                        {"label": "San Francisco", "value": "San Francisco"},
                        {"label": "Montreal", "value": "Montreal"}
                    ],
                    value=["San Francisco", "Montreal"],
                    labelStyle={"display": "inline-block"}
                ),
            ], style={"margin-left": "12%", "margin-top": "5%", "display": "inline-block"}),

            html.Div(
                [
                    html.P("Choose Country: "),
                    dcc.RadioItems(
                        id="Country",
                        options=[{"label": k, "value": k} for k in all_options.keys()],
                        value="All"
                    ),
                ],
                style={"margin-left": "10%", "margin-top": "5%", "display": "inline-block", "position": ""}),
        ]),

        html.Div([
            html.Div([
                dcc.Graph(
                    id="example-graph-1"
                )
            ], style={"display": "inline-block"}),

            html.Div([
                dcc.Graph(
                    id="example-graph-2"
                )
            ], style={"display": "inline-block"})
        ], style={"text-align": "center"})
    ])
)


@app.callback(
    dash.dependencies.Output('Cities', 'options'),
    [dash.dependencies.Input('Country', 'value')])
def set_cities_options(selected_country):
    return [{'label': i, 'value': i} for i in all_options[selected_country]]


@app.callback(
    dash.dependencies.Output('example-graph-1', 'figure'),
    [dash.dependencies.Input('Cities', 'value')])
def update_image_src(selector):
    data = []
    for city in selector:
        data.append({'x': city_data[city]['x'], 'y': city_data[city]['y'],
                     'type': 'bar', 'name': city})
    figure = {
        'data': data,
        'layout': {
            'title': 'Graph 1',
            'xaxis': dict(
                title='x Axis',
                titlefont=dict(
                    family='Courier New, monospace',
                    size=20,
                    color='#7f7f7f'
                )),
            'yaxis': dict(
                title='y Axis',
                titlefont=dict(
                    family='Helvetica, monospace',
                    size=20,
                    color='#7f7f7f'
                ))
        }
    }
    return figure


@app.callback(
    dash.dependencies.Output('example-graph-2', 'figure'),
    [dash.dependencies.Input('Cities', 'value')])
def update_image_src(selector):
    data = []
    for city in selector:
        data.append({'x': city_data[city]['x'], 'y': city_data[city]['y'],
                     'type': 'line', 'name': city})
    figure = {
        'data': data,
        'layout': {
            'title': 'Graph 2',
            'xaxis': dict(
                title='x Axis',
                titlefont=dict(
                    family='Courier New, monospace',
                    size=20,
                    color='#7f7f7f'
                )),
            'yaxis': dict(
                title='y Axis',
                titlefont=dict(
                    family='Helvetica, monospace',
                    size=20,
                    color='#7f7f7f'
                ))
        }
    }
    return figure


if __name__ == '__main__':
    app.run_server(port=5060)
