from datetime import date,datetime,timedelta
from random import random
import pandas as pd

df=pd.read_csv("C:/Users/adria/Documents/Proj_data_Sew/clientes.csv")

#función que  genera fechas aleatorias(llamar a la función)
def get_rnd_date(start, end, fmt):

  s = datetime.strptime(start, fmt)
  e = datetime.strptime(end, fmt)

  delta = e - s

  return s + timedelta(days=(random() * delta.days))

#crear una lista vacía 
nuevas_fechas_random=[]
#especificar el numero de elementos que va a tener la lista(filas del DF)
filas_df=df.shape[0]
filas_df
#crear el for para generar los valores la cantidad de veces conocida
#propuesta de list comprehension para el for:
#nuevas_fechas_random=[fecha_almacenada for fecha_almacenada in get_rnd_date("01/01/2017", "01/02/2017", "%d/%m/%Y")]
#print(nuevas_fechas_random)

lista_num=[]
for r in range(0,15):
    lista_num.append(r)
print(lista_num)
nueva_lista_num=[num+100 for num in range(0,15)]
print(nueva_lista_num)

nueva_lista_num=["contando "+str(num) for num in range(0,15)]
print(nueva_lista_num)

nueva_lista_num=[3 for _ in range(0,15)]
print(nueva_lista_num)

lista_holas=["Hola Adrianita" for _ in range(5)]
print(lista_holas)

elem_separados=[ letter +"?" for letter  in "hola"]
print(elem_separados)

nuevas_fechas=[get_rnd_date("01/01/2017", "01/02/2017", "%d/%m/%Y") for _ in range(filas_df)]
print(nuevas_fechas)

#Constitución del for para list comprehension 
#for n in range(filas_df):
    #fecha_almacenada=get_rnd_date("01/01/2017", "01/02/2017", "%d/%m/%Y")
    #nuevas_fechas_random.append(fecha_almacenada)

df['created_date']=nuevas_fechas
print(df.created_date)

df.to_csv("C:/Users/adria/Documents/Proj_data_Sew/Clientes_fechas_ran.csv",index=False)

    



