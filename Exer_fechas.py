# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 19:51:45 2022

@author: adria
"""
from datetime import datetime, timedelta
import pandas as pd

df=pd.read_csv("C:/Users/adria/Documents/Proj_data_Sew/clientes.csv")

df['created_date']=datetime.now()
fecha_actualizada=1
new_created_date=[]

for created_date_row in df.created_date:
    updated_date=created_date_row + timedelta(days=fecha_actualizada)
    new_created_date.append(updated_date)
    fecha_actualizada +=1
    
df['created_date']=new_created_date

print (df.head())

df.to_csv("C:/Users/adria/Documents/Proj_data_Sew/Clientes_modificado.csv",index=False)