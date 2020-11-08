# Internal modules
from config.data_management import load_document
from config import config
from graphs import graphs
from utils import Header

# External libraries
import dash_core_components as dcc
import dash_html_components as html


def create_layout(app, graphs, title):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Div(html.H5(title, style={"padding-left": "10px"}), className="inner-product2"),
                                    html.Br([]),
                                    html.P(load_document(config.TEXT_FILE),
                                        style={"color": "#000000"},
                                        className="row",
                                    ),
                                ],
                                className="product2",
                            )
                        ],
                        className="row",
                    ),
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        [list(graphs[0].keys())[0]], className="subtitle padded"
                                    ),
                                    dcc.Graph(
                                        id = 'graph-one-p1',
                                        figure = list(graphs[0].values())[0]
                                        )
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        list(graphs[1].keys())[0],
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id='graph-two-p1',
                                        figure = list(graphs[1].values())[0]
                                        )
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                     # Row 5
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        list(graphs[2].keys())[0], 
                                        className="subtitle padded"
                                    ),
                                    dcc.Graph(
                                        id = 'graph-three-p1',
                                        figure = list(graphs[2].values())[0]
                                        )
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        list(graphs[3].keys())[0],
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id = 'graph-four-p1',
                                        figure = list(graphs[3].values())[0]
                                        )
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                ],
                className="sub_page",
            ), 
        ],
        className="page",
    ), html.Div(
        [
            ### PAGE 2 ###
            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Div(html.H5(title, style={"padding-left": "10px"}), className="inner-product2"),
                                    html.Br([]),
                                    html.P(load_document(config.TEXT_FILE),
                                        style={"color": "#000000"},
                                        className="row",
                                    ),
                                ],
                                className="product2",
                            )
                        ],
                        className="row",
                    ),
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        [list(graphs[4].keys())[0]], className="subtitle padded"
                                    ),
                                    dcc.Graph(
                                        id = 'graph-one-p2',
                                        figure = list(graphs[4].values())[0]
                                        )
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        list(graphs[5].keys())[0],
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id='graph-two-p2',
                                        figure = list(graphs[5].values())[0]
                                        )
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                     # Row 5
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        list(graphs[6].keys())[0], 
                                        className="subtitle padded"
                                    ),
                                    dcc.Graph(
                                        id = 'graph-three-p2',
                                        figure = list(graphs[6].values())[0]
                                        )
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        list(graphs[7].keys())[0],
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id = 'graph-four-p2',
                                        figure = list(graphs[7].values())[0]
                                        )
                                ],
                                className="six columns",
                            ),
                            
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        list(graphs[8].keys())[0], 
                                        className="subtitle padded"
                                    ),
                                    dcc.Graph(
                                        id = 'graph-five-p2',
                                        figure = list(graphs[8].values())[0]
                                        )
                                ],
                                className="six columns",
                            ),
                                 html.Div(
                                [
                                    html.H6(
                                        list(graphs[9].keys())[0],
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id = 'graph-six-p2',
                                        figure = list(graphs[9].values())[0]
                                        )
                                ],
                                className="six columns",
                            ),
                            
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                ],
                className="sub_page",
            ), 
        ],
        className="page",
    )
