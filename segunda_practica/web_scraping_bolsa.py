import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import pandas as pd


def scraping():

    url_page = 'https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000&punto=indice'
    page = requests.get(url_page).text 
    soup = BeautifulSoup(page, "lxml")
    tabla = soup.find('table', attrs={'id': 'ctl00_Contenido_tblAcciones'})

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
                # print("Indice:", name)
            if nroCelda==2:
                price=celda.text
                # print("Valor:", price)
            nroCelda=nroCelda+1
        if name != 'Indice':
            df = df.append({'Indice':name, 'Valor':price, 'Fecha': datetime.now()}, ignore_index=True)
    # print(df)

    df.to_csv('exportacion.csv', index = False)

    return df

scraping()