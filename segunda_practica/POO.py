import requests
import re
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

class acciones:
    def __init__(self):
        self.url_page = "https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000&punto=indice"

    def scrap_madrid(self, url_page):
        page = requests.get(self.url_page).text
        soup = BeautifulSoup(page, "lxml")
        tabla = soup.find('table', attrs={'id': 'ctl00_Contenido_tblAcciones'})
    
        name = "Indice"
        price = "Valor"
        fecha = "Fecha"
        array = []
        df = pd.DataFrame(columns=['Indice', 'Valor', 'Fecha','URL','Ticker'])
        df2 = pd.DataFrame(columns=['Nombre', 'Link', 'Ticker'])
        nroFila=0
    
        for link in soup.find_all(attrs={'href': re.compile("^/esp/aspx/Empresas/FichaValor")}):
            nombre = link.text
            url = 'https://www.bolsamadrid.es'+link.get('href')
            df2 = df2.append({'Nombre': nombre,'Link': url} , ignore_index=True)
    
        for fila in tabla.find_all("tr"):
            nroCelda=0
            for celda in fila.find_all('td'):
                if nroCelda==0:
                    name=celda.text
                if nroCelda==2:
                    price=celda.text
                nroCelda=nroCelda+1
            if name != 'Indice':
                df = df.append({'Indice':name, 'Valor':price, 'Fecha': datetime.now()}, ignore_index=True)
    
        i = 0
        while i < int(len(df2)):
            self.url_page = df2['Link'][i]
            page = requests.get(self.url_page).text 
            soup = BeautifulSoup(page, "lxml")
            ticker = soup.find('td', attrs={'id': 'ctl00_Contenido_TickerDat'}).text
            df['Ticker'][i] = re.sub(r"\s+", "", (ticker +'.MC'))
            df['URL'][i] = self.url_page
            i = i+1
        
        return df

    def scrap_accion(self):
        # Scrap de la accion, le pasamos el ticker
        pass

    def guardar(self,df):
        self.df = df
        df.to_csv('exportacion.csv', index = False)
        print('Exportación completada')

    def leer(self):
        # Leer el CSV
        opendf = pd.read_csv('exportacion.csv')
        
        return opendf

    def graficar(self):
        # Graficar el estado de la accion, le pasamos el ticker
        pass

tarea = acciones()
tarea.leer()