# External libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Internal modules
from config import config
from pages import (pageOne, pageTwo, pageThree)
from config.data_management import load_excel
from graphs import graphs


df = load_excel(file_name=config.DATA_FILE) 
print(df.columns)


app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)

server = app.server
app.config.suppress_callback_exceptions = True
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    print(pathname)
    if pathname == "/report/pageTwo":
        return pageTwo.create_layout(app, 
                                     df, 
                                     graphs = [
                                         {'Target': graphs.barchart(df,'Target')},
                                         {'Rooms': graphs.barchart(df, 'rooms')},
                                         {'Years of Education': graphs.barchart(df, 'escolari')},
                                         {'Overcrowding Index': graphs.linechart(dataframe=df, variable='age-min', group_variable='Target')}
                                         ])
    elif pathname == "/report/pageThree":
        return pageThree.create_layout(app,df)
    else:
        return pageOne.create_layout(app)



    

if __name__ == "__main__":
    app.run_server(host='0.0.0.0',port=8050,debug=False)