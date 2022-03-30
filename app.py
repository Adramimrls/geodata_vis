# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 17:55:49 2022

@author: adria
"""
from dash import Dash, dash_table
import dash
import dash_core_components as dcc
import dash_html_components as html
#from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

clients_data = pd.read_csv("C:/Users/adria/Documents/Proj_data_Sew/clientes.csv")
store_data=pd.read_csv("C:/Users/adria/Documents/Proj_data_Sew/proveedores.csv")
df=pd.read_csv("C:/Users/adria/Documents/Proj_data_Sew/clientes.csv")

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
df_clientes = pd.read_csv("C:/Users/adria/Documents/Proj_data_Sew/Clientes_modificado.csv")
#se puede leer caulquier df creado en este código (revisar los existentes)

# creación del mapa 
fig = px.scatter_mapbox(all_data,
                        lat="coord_x", 
                        lon="coord_y", 
                        hover_name="name",
                        hover_data=["id", "service","clothes"],
                        color="type", zoom=12, height=600)

fig.update_layout(mapbox_style="open-street-map")

app = dash.Dash(__name__)
#a partir de aquí, se agrega lo que se desea mostrar
app.layout = html.Div(
    
    children=[
    html.H1(children='Datos de Clientes'),
    html.Div(children='''Prendas'''),
    
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [trace1, trace2, trace3, trace4,trace5,trace6],
            'layout':
            go.Layout(title='Estado de orden por cliente', barmode='stack')
        }),
    dcc.Graph(figure=fig),

    dash_table.DataTable(df_clientes.to_dict('records'), [{"name": i, "id": i} for i in df_clientes.columns]) 
   
])

if __name__ == '__main__':
    app.run_server(debug=True)
