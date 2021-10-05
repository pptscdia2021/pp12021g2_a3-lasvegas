import yfinance as yf
import pandas as pd

acciones = ["ANA.MC", "BBVA.MC", "GRF.MC", "ELE.MC","REP.MC"]

def scrapYahoo(acciones):
    df_list = list()

    # i = 0
    # while i < len(acciones):
    #     a = yf.Ticker(acciones[i])
    #     print(a.info['shortName'])
    #     i = i+1

    for ticker in acciones:
        data = yf.download(ticker, group_by='ticker', period='1d')
        data['ticker'] = ticker  
        df_list.append(data)

    df = pd.concat(df_list)
    
    df.to_csv('yahoo_finance.csv')
    return df
scrapYahoo(acciones)