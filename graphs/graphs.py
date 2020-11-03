# External libraries
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.figure_factory as ff
import pandas as pd
import numpy as np
import dash_table
from plotly.subplots import make_subplots

# Internal modules
from config import config
from graphs.layouts import STANDARD_GRAPH_LAYOUT


def StandardGraph(title, id, figure):
    return html.Div(
        [
            html.H6(
                [title], className="subtitle padded"),
                dcc.Graph(
                    id = id,
                    figure = figure)
        ],
        className="six columns")


#StandardGraph(title='Goat', id='graph-one', figure=graphs.barchart(data,'Target', 'roof'))

def barchart(dataframe, variable, group_variable=None, layout=STANDARD_GRAPH_LAYOUT):
    """
    Maximum 4 categories.
    """
    
    COLORS = ['#76323F','#d4d1d3','#565656','#C09F80']
    data = []
    
    if group_variable!=None:
        legend = True
        for group in list(dataframe[group_variable].unique()):
            data.append(
                go.Bar(
                    x = dataframe[dataframe[group_variable]==group][variable].value_counts(normalize=True).index,
                    y = dataframe[dataframe[group_variable]==group][variable].value_counts(normalize=True).values,

                    marker = {
                        'color': COLORS[group],
                        'line': {
                            'color': 'rgb(255, 255, 255)',
                            'width': 2}
                    },
                    name = f"{group_variable} = {group}"
                )
            )
    else: 
        legend = False
        data = go.Bar(
                    x = dataframe[variable].value_counts(normalize=True).index,
                    y = dataframe[variable].value_counts(normalize=True).values,

                    marker = {
                        'color': COLORS[0],
                        'line': {
                            'color': 'rgb(255, 255, 255)',
                            'width': 2}
                    }
                )
    
    figure = go.Figure(data=data, layout=layout)
    
    return figure