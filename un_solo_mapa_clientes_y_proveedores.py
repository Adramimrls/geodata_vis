# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 19:25:33 2022

@author: adria
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

clients_data = pd.read_csv("C:/Users/adria/Documents/Proj_data_Sew/clientes.csv")
store_data=pd.read_csv("C:/Users/adria/Documents/Proj_data_Sew/proveedores.csv")

store_data.rename(columns={"handle_clothes":"clothes"}, inplace=True)
store_data=store_data.rename({"handle_clothes":"clothes"})
all_data=pd.concat([store_data,clients_data])
print(all_data)

fig = px.scatter_mapbox(all_data,
                        lat="coord_x", 
                        lon="coord_y", 
                        hover_name="name",
                        hover_data=["id", "service","clothes"],
                        color="type", zoom=12, height=600)

fig.update_layout(mapbox_style="open-street-map")

app = dash.Dash(__name__)

app.layout = html.Div([
    
    dcc.Graph(figure=fig)
])


if __name__ == '__main__':
    app.run_server(debug=True)



