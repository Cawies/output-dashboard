# External libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Internal modules
from config import config
from pages import (pageOne, pageTwo, pageThree, pageFour)
from config.data_management import load_excel
from graphs import graphs


df = load_excel(file_name=config.DATA_FILE) 
model_performance = load_excel(file_name='model_performances.xlsx')


app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)

server = app.server
app.config.suppress_callback_exceptions = True
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

#distplot(dataframe, variable, group_variable=None, layout=STANDARD_DISTPLOT_LAYOUT)

# RETURN SELECTED PAGE
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    print(pathname)
    if pathname == "/report/pageTwo":
        return pageTwo.create_layout(app=app, 
                                     title='Predictor variable distributions',
                                     graphs = [
                                         {'Poverty Level': graphs.barchart(df,'Target')},
                                         {'Number of Rooms': graphs.barchart(df, 'rooms')},
                                         {'Roof Quality': graphs.barchart(df, 'roof')},
                                         {'Overcrowding Index': graphs.distplot(dataframe=df, variable='overcrowding')},
                                         {'Lowest Education in years': graphs.distplot(df,'escolari-min')},
                                         {'Highest Education in years': graphs.distplot(df, 'escolari-max')},
                                         {'Total Years of Education': graphs.distplot(df, 'escolari-sum')},
                                         {'Years of Education Head of Household': graphs.distplot(dataframe=df, variable='escolari')},
                                         {'Youngest household member age': graphs.distplot(dataframe=df, variable='age-min')},
                                         {'Household age variation': graphs.distplot(dataframe=df, variable='age-std')}
                                         ])
    elif pathname == "/report/pageThree":
        return pageThree.create_layout(app=app,
                                       title='Predictor by Target distributions',
                                       graphs = [ 
                                         {'Poverty Level': graphs.barchart(df,'Target')},
                                         {'Number of Rooms': graphs.barchart(df, 'rooms', 'Target')},
                                         {'Roof Quality': graphs.barchart(df, 'roof', 'Target')},
                                         {'Overcrowding Index': graphs.distplot(dataframe=df, variable='overcrowding', group_variable='Target')},
                                         {'Lowest Education in years': graphs.distplot(df,'escolari-min', 'Target')},
                                         {'Highest Education in years': graphs.distplot(df, 'escolari-max', 'Target')},
                                         {'Total Years of Education': graphs.distplot(df, 'escolari-sum', 'Target')},
                                         {'Years of Education Head of Household': graphs.distplot(dataframe=df, variable='escolari', group_variable='Target')},
                                         {'Youngest household member age': graphs.distplot(dataframe=df, variable='age-min', group_variable= 'Target')},
                                         {'Household age variation': graphs.distplot(dataframe=df, variable='age-std', group_variable='Target')}
                                           ])
    elif pathname == "/report/pageFour":
        return pageFour.create_layout(app = app, 
                                      title='Model Benchmarking',
                                      graphs = [
                                          {'model_benchmarks': graphs.multivar_barchart(model_performance, 'model', ['mean_train_acc', 'mean_test_acc', 'mean_train_acc_tuned','mean_test_acc_tuned'])},
                                          {'model_benchmarks': graphs.multivar_barchart(model_performance, 'model', ['mean_train_acc', 'mean_test_acc', 'mean_train_acc_tuned','mean_test_acc_tuned'])},
                                          {'model_benchmarks': graphs.multivar_barchart(model_performance, 'model', ['mean_train_acc', 'mean_test_acc', 'mean_train_acc_tuned','mean_test_acc_tuned'])},
                                          {'model_benchmarks': graphs.multivar_barchart(model_performance, 'model', ['mean_train_acc', 'mean_test_acc', 'mean_train_acc_tuned','mean_test_acc_tuned'])}
                                          
                                      ])
                                         
    else:
        return pageOne.create_layout(app)

    

if __name__ == "__main__":
    app.run_server(host='0.0.0.0',port=8050,debug=False)