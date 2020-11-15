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
from graphs.layouts import STANDARD_GRAPH_LAYOUT, STANDARD_LINEGRAPH_LAYOUT, STANDARD_DISTPLOT_LAYOUT

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
                    x = dataframe[dataframe[group_variable]==group][variable].value_counts(normalize=True).sort_index().index,
                    y = dataframe[dataframe[group_variable]==group][variable].value_counts(normalize=True).sort_index().values,

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
                    x = dataframe[variable].value_counts(normalize=True).sort_index().index,
                    y = dataframe[variable].value_counts(normalize=True).sort_index().values,

                    marker = {
                        'color': COLORS[0],
                        'line': {
                            'color': 'rgb(255, 255, 255)',
                            'width': 2}
                    }
                )
    
    figure = go.Figure(data=data, layout=layout)
    
    return figure


def linechart(dataframe, variable, group_variable=None, layout=STANDARD_LINEGRAPH_LAYOUT):
    
    COLORS = ['#76323F','#d4d1d3','#565656','#C09F80']
    data = []
    
    if group_variable!=None:
        legend = True
        for group in list(dataframe[group_variable].unique()):
            data.append(
                go.Scatter(
                    x = dataframe[dataframe[group_variable]==group][variable].value_counts().sort_index().index,
                    y = dataframe[dataframe[group_variable]==group][variable].value_counts().sort_index().values,
                    line = {'color': COLORS[group], 'smoothing':1, 'shape': 'spline'},
                    mode = 'lines',
                    name = f"{group_variable} = {group}"
        )
            )
    else: 
        legend = False
        data =  go.Scatter(
            x = dataframe[variable].value_counts().sort_index().index,
            y = dataframe[variable].value_counts().sort_index().values,
            line = {'color': '#97151c', 'smoothing':1, 'shape': 'spline'},
            mode = 'lines',
            name = variable
        )

    
    yaxis = {
        'autorange': True,
        'gridcolor': 'rgba(127, 127, 127, 0.2)',
        'mirror': False,
        'nticks': 4,
        'showgrid': True,
        'showline': True,
        'ticklen': 5,
        'ticks': 'outside',
        'title': 'Label me!',
        'type': 'linear',
        'zeroline': False,
        'zerolinewidth': 4
    }
    
    fig = go.Figure(data=data, layout=layout)
    
    return fig


def distplot(dataframe, variable, group_variable=None, layout=STANDARD_DISTPLOT_LAYOUT):
    COLORS = ['#76323F','#d4d1d3','#565656','#C09F80']
    data = []
    
    if group_variable==None:
        data.append(dataframe[variable].values)
        figure = ff.create_distplot(data, [variable], show_hist=True, show_rug=False, colors=COLORS)
    else:
        group_labels = []
        for group in list(dataframe[group_variable].unique()):
            data.append(dataframe[dataframe[group_variable]==group][variable].values)
            group_labels.append(f"{group_variable} = {group}")
        figure = ff.create_distplot(data, group_labels, show_hist=False, show_rug=False, colors=COLORS)
        
        
    figure.update_layout(layout)
        
    

    
    return figure

def multivar_barchart(dataframe, category, variables, layout=STANDARD_GRAPH_LAYOUT):
    COLORS = ['#76323F','#d4d1d3','#565656','#C09F80']
    data = []
    
    for variable in range(len(variables)):
        data.append(
            go.Bar(
                x = dataframe[category],
                y = dataframe[variables[variable]],
                                    marker = {
                        'color': COLORS[variable],
                        'line': {
                            'color': 'rgb(255, 255, 255)',
                            'width': 0.5}
                    }
            )
        )
    
    figure = go.Figure(data=data, layout=layout)
    
    return figure