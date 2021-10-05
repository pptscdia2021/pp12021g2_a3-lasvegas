import yfinance as yf
import pandas as pd

def scrapYahoo(acciones):
    df_list = list()

    for ticker in acciones:
        data = yf.download(ticker, group_by='ticker', period='1d')
        data['ticker'] = ticker  
        df_list.append(data)

    df = pd.concat(df_list)
    
    df.to_csv('yahoo_finance.csv')
    return df