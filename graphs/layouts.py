# External libraries
import plotly.graph_objs as go

COLORSCALE_SMALL = ['#76323F',
                    '#d4d1d3',
                    '#565656',
                    '#C09F80']

COLORSCALE_LARGE = ['#76323f',
                    '#7d3c45', 
                    '#84464b', 
                    '#8a4f51', 
                    '#915957', 
                    '#97635e', 
                    '#9e6c65', 
                    '#a4766d', 
                    '#ab8075', 
                    '#b18a7e', 
                    '#b79487', 
                    '#bc9e91', 
                    '#c2a89c', 
                    '#c7b2a8', 
                    '#ccbcb4', 
                    '#d0c7c3', 
                    '#d4d1d3']

STANDARD_GRAPH_LAYOUT = go.Layout(
    template = 'plotly_white',
    autosize = False,
    bargap = 0.35,
    font = {
        'family': 'Raleway',
        'size': 10
    },
    height = 200,
    legend = {
        'x': -0.0228945952895,
        'y': -0.189563896463,
        'orientation': 'h',
        'yanchor': 'top'
    },
    margin = {
        'r': 0,
        't': 20,
        'b': 10,
        'l': 10
    },
    showlegend = False,
    title = '',
    width = 330,

    xaxis = {
        'autorange': True,
        'showline': True,
        'title': '',
        'type': 'category'
    },
    yaxis = {
        'autorange': True,
        'showgrid': True,
        'showline': True,
        'title': '',
        'type': 'linear',
        'zeroline': False
    },
    transition = {
            'duration': 500,
            'easing': 'cubic-in-out'
        }
)

STANDARD_LINEGRAPH_LAYOUT = go.Layout(
        template = 'plotly_white',
        autosize = True,
        title = '',
        font = {
            'family': 'Raleway',
            'size': 10
        },
        height = 200,
        width = 340,
        hovermode = 'closest',
        legend = {
            'x': -0.0277108433735,
            'y': -0.142606516291,
            'orientation': 'h'
        },
        margin = {
            'r': 20,
            't': 20,
            'b': 20,
            'l': 50
        },
        showlegend = True,
        xaxis = {
            'autorange': True,
            'linecolor': 'rgb(0, 0, 0)',
            'linewidth': 1,
            'showgrid': False,
            'showline': True,
            'title': '',
            'type': 'linear',
        }
    )

STANDARD_DISTPLOT_LAYOUT = go.Layout(
    template = 'plotly_white',
    autosize = True,
    title = '',
    font = {
        'family': 'Raleway',
        'size': 10
    },
    height = 200,
    width = 340,
    hovermode = 'closest',
    legend = {
        'x': -0.0277108433735,
        'y': -0.142606516291,
        'orientation': 'h'
    },
    margin = {
        'r': 20,
        't': 20,
        'b': 20,
        'l': 50
    },
    showlegend = True,
    xaxis = {
        'autorange': True,
        'linecolor': 'rgb(0, 0, 0)',
        'linewidth': 1,
        'showgrid': False,
        'showline': True,
        'title': '',
        'type': 'linear',
    })