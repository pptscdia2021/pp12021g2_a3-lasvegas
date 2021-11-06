import requests
import re
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
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

    def scrap_accion(self,accion):
        df_list = list()

        for ticker in accion:
            data = yf.download(ticker, group_by='ticker', period='1d')
            data['ticker'] = ticker  
            df_list.append(data)
    
        df = pd.concat(df_list)
        print(df)


    def guardar(self,df):
        self.df = df
        df.to_csv('exportacion.csv', index = False)
        print('Exportación completada')

    def leer(self):
        # Leer el CSV
        opendf = pd.read_csv('exportacion.csv')
        print(opendf)

    def listado_acciones(self):
        # Lee el CSV
        opendf = pd.read_csv('exportacion.csv')

        # Crea una lista con los tickers
        lista = opendf['Ticker']
        print(lista)

    def graficar(self,df,catidad):
        print(df)
        tiko = df['Ticker']

        i = 0
        while i < catidad:
            tic = yf.Ticker(tiko[i])
            dibuDf = tic.history(period = "5y")
            dibuDf['Close'].plot(title = tiko[i])
            i = i + 1
            plt.show()

tarea = acciones()

# Scraping por aaciones
# tarea.scrap_accion(['AAPL','MSFT','GOOG','FB'])

# Graficar 2 desde el Scraping
# tarea.graficar(tarea.scrap_madrid(tarea.url_page))

# Graficar 2 aaccion
# tarea.graficar({'Ticker':['ANA.MC','AENA.MC']},2)

# Graficar 1 aaccion
#tarea.graficar({'Ticker':['ANA.MC']},1)

# Leer el CSV
# tarea.leer()

# Listado de acciones
# tarea.listado_acciones()