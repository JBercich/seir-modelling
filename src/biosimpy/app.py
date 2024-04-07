#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from dash import Dash, html, dcc, Output, Input
import dash_bootstrap_components as dbc

app: Dash = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("BioSimPy", className="display-4"),
        html.P("Computer simulations of biological systems.", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("Overview", href="/", active="exact"),
                dbc.NavLink("Epidemiology", href="/epidemiology", active="exact"),
                dbc.NavLink("Neuroscience", href="/neuroscience", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.Div([html.H2("Overview", className="display-6"), html.Hr()])
    elif pathname == "/epidemiology":
        return html.Div([html.H2("Epidemiology", className="display-6"), html.Hr()])
    elif pathname == "/neuroscience":
        return html.Div([html.H2("Neuroscience", className="display-6"), html.Hr()])
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"Pathname {pathname} was not recognised."),
        ],
        className="p-3 bg-light rounded-3",
    )


if __name__ == "__main__":
    app.run(debug=True)
