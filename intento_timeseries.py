
import plotly.express as px
import pandas as pd
import os

base_path = os.getcwd()
base_path = os.path.join(base_path, 'resources')
df_clientes_path = os.path.join(base_path,'Clientes_modificado.csv')

df_grafica = pd.read_csv (df_clientes_path)
print(df_grafica.head())
fig_timeseries = px.line(df_grafica, x='created_date', y="cant_prendas")
fig_timeseries.show()