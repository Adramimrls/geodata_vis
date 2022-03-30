# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 19:22:33 2022

@author: adria
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

store_data = pd.read_csv("C:/Users/adria/Downloads/store_data_good.csv")
print(store_data)

fig = px.scatter_mapbox(store_data,
                        lat="lati", 
                        lon="longi", 
                        hover_name="Name",
                        hover_data=["Id", "Service"],
                        color_discrete_sequence=["fuchsia"], zoom=12, height=600)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

app = dash.Dash(__name__)

app.layout = html.Div([
    
    dcc.Graph(figure=fig)
])


if __name__ == '__main__':
    app.run_server(debug=True)