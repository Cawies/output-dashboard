# Internal modules
from config.data_management import load_document
from config import config
from graphs import graphs
from utils import Header

# External libraries
import dash_core_components as dcc
import dash_html_components as html


def create_layout(app, data):
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
                                    html.Div(html.H5("Associations", style={"padding-left": "10px"}), className="inner-product2"),
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
                                        ["Title"], className="subtitle padded"
                                    ),
                                    dcc.Graph(
                                        id = 'graph-one-p1',
                                        figure = graphs.barchart(data,'Target', 'roof')
                                        )
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Title",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id='graph-two-p1',
                                        figure = graphs.barchart(data,'Target', 'roof')
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
                                        ["Title"], 
                                        className="subtitle padded"
                                    ),
                                    dcc.Graph(
                                        id = 'graph-three-p1',
                                        figure = graphs.barchart(data,'Target', 'roof')
                                        )
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Title",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id = 'graph-four-p1',
                                        figure = graphs.barchart(data,'Target', 'roof')
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
