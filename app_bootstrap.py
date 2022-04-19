# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 17:55:49 2022

@author: adria
"""
from http import client
from dash import Dash, dash_table
import dash
import dash_core_components as dcc
import dash_html_components as html
#from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import os 
#import geopandas as gpd
#import earthpy as et
#import shapely

import dash_bootstrap_components as dbc



base_path = os.getcwd()
base_path = os.path.join(base_path, 'resources')
clients_data_path = os.path.join(base_path, 'clientes.csv')
store_data_path = os.path.join(base_path,'proveedores.csv')
df_clientes_path = os.path.join(base_path,'Clientes_modificado.csv')


clients_data = pd.read_csv(clients_data_path)
store_data=pd.read_csv(store_data_path)
df=pd.read_csv(clients_data_path)

#lectura de código html creado en el otro proyecto
with open('C:/Users/adria/Documents/Proj_Tianguis/mapas/mapa.html',"r") as f:
    mapa_prueba=f.read()

#Crear una tabla dinámica
pv= pd.pivot_table(df, index=['name'], columns=["clothes"], values=['cant_prendas'])
trace1 = go.Bar(x=pv.index, y=pv[('cant_prendas', 'cortina')], name='cortina')
trace2 = go.Bar(x=pv.index, y=pv[('cant_prendas', 'pantalon')], name='pantalon')
trace3 = go.Bar(x=pv.index, y=pv[('cant_prendas', 'vestido')], name='vestido')
trace4 = go.Bar(x=pv.index, y=pv[('cant_prendas', 'camisa')], name='camisa')
trace5 = go.Bar(x=pv.index, y=pv[('cant_prendas', 'falda')], name='falda')
trace6 = go.Bar(x=pv.index, y=pv[('cant_prendas', 'chamarra')], name='chamarra')

#ajuste de columnas
store_data.rename(columns={"handle_clothes":"clothes"}, inplace=True)
store_data=store_data.rename({"handle_clothes":"clothes"})
all_data=pd.concat([store_data,clients_data])
# print(all_data)

#creacion de dataframe con datos de clientes 
df_clientes = pd.read_csv(df_clientes_path)
#se puede leer caulquier df creado en este código (revisar los existentes)

# creación del mapa 
fig = px.scatter_mapbox(all_data,
                        lat="coord_x", 
                        lon="coord_y", 
                        hover_name="name",
                        hover_data=["id", "service","clothes"],
                        color="type", zoom=12, height=600)

fig.update_layout(mapbox_style="open-street-map")
#para agregar un shape
#mapa = gpd.read_file('C:/Users/adria/Documents/Proj_Tianguis/Del_GAM.shp')
#mapa.plot()


#timeseries
df_grafica = pd.read_csv (df_clientes_path)
print(df_grafica.head())
fig_timeseries = px.line(df_grafica, x='created_date', y="cant_prendas",markers=True, title='Cantidad de prendas solicitadas por día ')


app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
#a partir de aquí, se agrega lo que se desea mostrar
app.layout = dbc.Container(
    
    children=[
    html.H1(children='Análisis y visualización de datos geográficos con Python, un proyecto de Adriana Ramirez Morales.'),
    html.Div(children='''En el último año mi interés se ha dirigido a los Sistemas de Información Geográfica 
    y el análisis de datos, como herramienta para esto último elegí Python; a continuación ejemplifico lo aprendido.\n\n
    El objetivo de este proyecto es favorecer el uso del servicio de costura y reparación de prendas de vestir para maximizar su uso
    y disminuir la adquisisción de un producto completamente nuevo de una de las industrias más contaminantes en el mundo,
    lo anterior a través de la vinculación de las personas interesadas en reciclar/transformar/reparar sus prendas de vestir y un "proveedor" 
    de este servicio (con una máquina de coser) a través de una aplicación como muchas que existen actualmente, pero enfocada en 
    esta actividad.\n
    Por el momento, los datos con que se cuentan son de uso didáctico, coordenadas, nombres de clientes y establecimientos aleatorios para 
    realizar distintos ejercicios.'''),
    dbc.Row([
        dbc.Col(html.Div("columna 1")),
        dbc.Col(html.Div("columna 2")),
        dbc.Col(html.Div("columna 3")),
    ]),
    html.Br(),
    dbc.Row([dbc.Col(html.Div([
        html.H1(children='Ubicación de clientes y proveedores'),
        html.Div(children='''Visualización de datos geográficos de clientes y proveedores, utilizando Open Street Map como base'''),
        #En esta parte quiero agregar el shape de la delegación Gustavo A. Madero previamente extraida de la capa de municipios a nivel nacional,
        #disponible en el portal de la CONABIO
        dcc.Graph(figure=fig),

        ])),
        dbc.Col(html.Div([
            html.H1(children='Gráfica interactiva'),
            html.Div(children='''Muestra la cantidad de prendas que cada cliente desea someter a alguna de las 2 categorías establecidas 
            hasta el momento, definidas como reparación y transformación; se utiliza un color distinto para cada una de las 6 opciones de 
            prenda a aceptar'''),

            dcc.Graph(
                id='example-graph',
                figure={
                    'data': [trace1, trace2, trace3, trace4,trace5,trace6],
                    'layout':
                    go.Layout(title='Cantidad de prendas por cliente', barmode='stack')
                }),

        ]))
        ]),
    
    
    
    html.H1(children='Timeseries'),
    html.Div(children='''A partir de este comportamiento se pueden detectar valores mínimos y máximos para estimar la periodicidad 
    de eventos a lo largo del tiempo.'''),
    dcc.Graph(figure=fig_timeseries),
    
    html.H1(children='DataFrame'),
    html.Div(children='''Detalle de la información utilizada'''),
    dash_table.DataTable(df_clientes.to_dict('records'), [{"name": i, "id": i} for i in df_clientes.columns]),
    html.Iframe(id='map', srcDoc=mapa_prueba, width='100%', height='600') #agregar código alóctono (embeber)
   
])

if __name__ == '__main__':
    app.run_server(debug=True)

