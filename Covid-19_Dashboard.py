import math
import pandas as pd
import numpy as np
import time

import matplotlib.pylab as plt
import plotly.graph_objs as go
import plotly.offline as py
import seaborn as sns;

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from sklearn.impute import SimpleImputer

plt.style.use('fivethirtyeight')


df = pd.read_csv('Covid19 Final Data.csv', header=0)
df.style.format({"Date": lambda t: t.strftime("%d-%m-%Y")})
states = df['State'].unique()

app = dash.Dash(__name__)

app.layout = html.Div([
    
    html.Div([

        html.Br(),
        html.Div(id='output_data'),
        html.Br(),

        html.Label(['Choose the name of the State:'],style={'font-weight': 'bold', "text-align": "center"}),

        dcc.Dropdown(id='my_dropdown',
            options=[
                {'label': 'Andaman and Nicobar Islands', 'value': 'Andaman and Nicobar Islands'}, {'label': 'Andhra Pradesh', 'value': 'Andhra Pradesh'},
                {'label': 'Arunachal Pradesh', 'value': 'Arunachal Pradesh'}, {'label': 'Assam', 'value': 'Assam'},
                {'label': 'Bihar', 'value': 'Bihar'}, {'label': 'Chandigarh', 'value': 'Chandigarh'},
                {'label': 'Chhattisgarh', 'value': 'Chhattisgarh'}, {'label': 'Dadra and Nagar Haveli and Daman and Diu', 'value': 'Dadra and Nagar Haveli and Daman and Diu'},
                {'label': 'Delhi', 'value': 'Delhi'}, {'label': 'Goa', 'value': 'Goa'},
                {'label': 'Gujarat', 'value': 'Gujarat'}, {'label': 'Haryana', 'value': 'Haryana'},
                {'label': 'Himachal Pradesh', 'value': 'Himachal Pradesh'}, {'label': 'Jammu and Kashmir', 'value': 'Jammu and Kashmir'},
                {'label': 'Jharkhand', 'value': 'Jharkhand'}, {'label': 'Karnataka', 'value': 'Karnataka'},
                {'label': 'Kerala', 'value': 'Kerala'}, {'label': 'Ladakh', 'value': 'Ladakh'},
                {'label': 'Lakshadweep', 'value': 'Lakshadweep'}, {'label': 'Madhya Pradesh', 'value': 'Madhya Pradesh'},
                {'label': 'Maharashtra', 'value': 'Maharashtra'}, {'label': 'Manipur', 'value': 'Manipur'},
                {'label': 'Meghalaya', 'value': 'Meghalaya'}, {'label': 'Mizoram', 'value': 'Mizoram'},
                {'label': 'Nagaland', 'value': 'Nagaland'}, {'label': 'Odisha', 'value': 'Odisha'},
                {'label': 'Puducherry', 'value': 'Puducherry'}, {'label': 'Punjab', 'value': 'Punjab'},
                {'label': 'Rajasthan', 'value': 'Rajasthan'}, {'label': 'Sikkim', 'value': 'Sikkim'},
                {'label': 'Tamil Nadu', 'value': 'Tamil Nadu'}, {'label': 'Telengana', 'value': 'Telengana'},
                {'label': 'Tripura', 'value': 'Tripura'}, {'label': 'Uttar Pradesh', 'value': 'Uttar Pradesh'},
                {'label': 'Uttarakhand', 'value': 'Uttarakhand'}, {'label': 'West Bengal', 'value': 'West Bengal'},
            ],
            optionHeight=35,                    #height/space between dropdown options
            value='Borough',                    #dropdown value selected automatically when page loads
            disabled=False,                     #disable dropdown value selection
            multi=False,                        #allow multiple dropdown values to be selected
            searchable=True,                    #allow user-searching of dropdown values
            search_value='',                    #remembers the value searched in dropdown
            placeholder='Please select...',     #gray, default text shown when no option is selected
            clearable=True,                     #allow user to removes the selected value
            style={'width':"45%"},              #use dictionary to define CSS styles of your dropdown
            # className='select_box',           #activate separate CSS document in assets folder
            # persistence=True,                 #remembers dropdown value. Used with persistence_type
            # persistence_type='memory'         #remembers dropdown value selected until...
            ),                                  #'memory': browser tab is refreshed
                                                #'session': browser tab is closed
                                                #'local': browser cookies are deleted
    ],className='one column'),
	
	html.Div([
        dcc.Graph(id='covid_graph')
    ], className='three columns'),

])

#---------------------------------------------------------------
# Connecting the Dropdown values to the graph
@app.callback(
    Output(component_id='covid_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)

def build_graph(column_chosen):
    C = pd.DataFrame()
    state = column_chosen
    fig = go.Figure()
    for idx in range(0,len(states)):
        if states[idx] == state:
            C = df[df['State']==states[idx]].reset_index()
    fig.add_trace(go.Scatter(x=C['Date'],y=C['Confirmed'],name='Confirmed Rate'))
    fig.add_trace(go.Scatter(x=C['Date'],y=C['Deaths'],name='Death Rate'))
    fig.add_trace(go.Scatter(x=C['Date'],y=C['Recovered'],name='Recovered Rate'))

    GraphTitle = "Covid-19 Trend in "+state
    fig.update_layout(
        title=GraphTitle,
        xaxis_title="Dates", width=1000, height=550,
        yaxis_title="Number of cases",
        font=dict(
            family="Courier New, monospace",
            size=12,
            color="#7f7f7f"
        ))
    return fig
#---------------------------------------------------------------
# For tutorial purposes to show the user the search_value

@app.callback(Output(component_id='output_data', component_property='children'), [Input(component_id='my_dropdown', component_property='search_value')])

def build_graph(data_chosen):
    return (format(data_chosen))
#---------------------------------------------------------------

if __name__ == "__main__":
	app.run_server(debug=True)