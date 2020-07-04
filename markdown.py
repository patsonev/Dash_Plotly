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
    ),

    html.Button("Submit", id="submit_form"),

    html.Br(),
    html.Br(),

    dcc.Markdown(
        """
        ### Dash markup 
        Dash support [Markdown](https://dev.to/amigosmaker/what-is-the-largest-site-created-using-flask-3214)
        Markdown is a simple way to write and format text.
        
        It includes a syntax for things like **bold**  and *italic* text,
        [link](https://www.youtube.com/watch?v=tpkZqE_cJsE&list=PLoqKVGJFXt27WhizoRfAQ0USvJ3bIRqDW&index=67), inline
        `code` snippets, and more.
        """
    )
])

if __name__ == "__main__":
    app.run_server(port=5050)
