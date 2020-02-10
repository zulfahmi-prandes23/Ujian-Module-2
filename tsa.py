import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import seaborn as sns
import dash_table


def generate_table(dataframe, page_size=10):
    return dash_table.DataTable(
        id='dataTable',
        columns=[{
            "name": i,
            "id": i
        } for i in dataframe.columns],
        data=dataframe.to_dict('records'),
        page_action="native",
        page_current=0,
        page_size=page_size,
    )


tsa = pd.read_csv('tsa_claims_ujian.csv')
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    children=[
        html.H1('Ujian Module 2 Dashboard TSA'),
        html.Div(children='''
        Created by: Zulfahmi
    '''),
        dcc.Tabs(
            children=[
                dcc.Tab(
                    value='Tab1',
                    label='DataFrame Table',
                        children=[
                            html.Div([
                                html.P('Max Rows:'),
                                dcc.Input(id ='filter-row',
                                            type = 'number', 
                                            value = 10)
                                ], className = 'row col-1'),
                                
                                html.Div(children =[
                                        html.Button('search',id = 'filter')
                                ],className = 'row col-2'),
                                
                                html.Div(id='div-table',
                                        children=[generate_table(tsa)])
                            ])
                dcc.Tab(
                    children=[
                        dcc.Tab(
                            value='Tab2',
                            label='Bar-Chart',
                            children=[
                                html.Div([
                                    dcc.Graph(id='Bar-Chart',
                                            figure={
                                                'data': [{
                                                    'X': tsa['Claim Amount'],
                                                    'Y': tsa['Close Amount'],
                                                    'type': 'bar',
                                                    'name': 'Property Damage'
                                                }, {
                                                    'X': tsa['Claim Amount'],
                                                    'Y': tsa['Close Amount'],
                                                    'type': 'bar',
                                                    'name': 'Passenger Property Loss'
                                                }, {
                                                    'X': tsa['Claim Amount'],
                                                    'Y': tsa['Close Amount'].
                                                    'type': 'bar',
                                                    'name': 'Employee Loss (MPCECA)'
                                                }, {
                                                    'X': tsa['Claim Amount'],
                                                    'Y': tsa['Close Amount'].
                                                    'type': 'bar',
                                                    'name': 'Passenger Theft'
                                                }]
                                            })
                                ])
                            ]),
                dcc.Tab(
                    value='Tab3',
                    label='Scatter Chart',
                    children=[
                        html.Div(children=dcc.Graph(
                            id='graph-scatter',
                            figure={
                                'data': [
                                    go.Scatter

    #### Mohon maaf mas untuk seterusnya belum selesai, dan bagian yang atas masih belum sesuai

            ## Tabs Content Style
            content_style={
                'fontFamily': 'Arial',
                'borderBottom': '1px solid #d6d6d6',
                'borderLeft': '1px solid #d6d6d6',
                'borderRight': '1px solid #d6d6d6',
                'padding': '44px'
            })
    ],
    #Div Paling luar Style
    style={
        'maxWidth': '1200px',
        'margin': '0 auto'
    })

if __name__ == '__main__':
    app.run_server(debug=True)