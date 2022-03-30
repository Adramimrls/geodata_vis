# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 19:34:53 2022

@author: adria
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

client_data = pd.read_csv("C:/Users/adria/Documents/Proj_data_Sew/clientes.csv")
print(client_data)

fig = px.scatter_mapbox(client_data,
                        lat="coord_x", 
                        lon="coord_y", 
                        hover_name="name",
                        hover_data=["id", "service","clothes"],
                        color_discrete_sequence=["fuchsia"], zoom=12, height=600)
fig.update_layout(mapbox_style="open-street-map")
#fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

proveedores_data = pd.read_csv("C:/Users/adria/Documents/Proj_data_Sew/proveedores.csv")
print(proveedores_data)

figura = px.scatter_mapbox(proveedores_data,
                        lat="coord_x", 
                        lon="coord_y", 
                        hover_name="name",
                        hover_data=["id", "service","handle_clothes"],
                        color_discrete_sequence=["fuchsia"], zoom=12, height=600)
figura.update_layout(mapbox_style="open-street-map")
#fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

app = dash.Dash(__name__)

app.layout = html.Div([
    
    dcc.Graph(figure=fig),
    dcc.Graph(figure=figura)
])


if __name__ == '__main__':
    app.run_server(debug=True)