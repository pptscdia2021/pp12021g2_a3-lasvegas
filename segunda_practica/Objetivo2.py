#instalar primero pip finance
# Importando librerias
# Si es necesario: pip install BeautifulSoup
# Si es necesario: pip install datetime

from bs4.element import ProcessingInstruction
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import pandas as pd

url_page = 'https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000&punto=indice'

page = requests.get(url_page).text 
soup = BeautifulSoup(page, "lxml")

tabla = soup.find('table', attrs={'id': 'ctl00_Contenido_tblAcciones'})

print(tabla)

name="Indice"
price="Valor"
fecha= "Fecha"
array = []
df = pd.DataFrame(columns=['Indice', 'Valor', 'Fecha'])
nroFila=0

for fila in tabla.find_all("tr"):
    #for row in  tabla.find_all("td")::
    nroCelda=0
    for celda in fila.find_all('td'):
        if nroCelda==0:
            name=celda.text
            print("Indice:", name)
        if nroCelda==2:
            price=celda.text
            print("Valor:", price)
        nroCelda=nroCelda+1
    if name != 'Indice':
        df = df.append({'Indice':name, 'Valor':price, 'Fecha': datetime.now()}, ignore_index=True)

print(df)

df.to_csv('exportacion.csv', index = False)

print("------- Df ordenado de mayor a menor los valores -------------------")
dfOrderValor = df.sort_values('Valor',ascending=False)
print(dfOrderValor)

print("----- Los dos máximos valores son: -----")
print(dfOrderValor['Valor'][8])
print(dfOrderValor['Valor'][19])

print("----- Los dos mínimos valores son: -----")
print(dfOrderValor['Valor'][20])
print(dfOrderValor['Valor'][34])

"""
# Me imprime sólo el máximo y mínimo (no los dos)
maximo = df.max()
minimo = df.min()

print("maximo-----------------")
print(maximo)
print("minimo-----------------")
print(minimo)"""
