# Crear la función comparativa y check
import matplotlib.pyplot as plt
import yfinance as yf

def comparativa(df):
    ticker = df['Ticker']
    #print(ticker)
    i = 0
    while i < int(len(ticker)):   
        tic = yf.Ticker(ticker[i])
        i = i + 1
        aapl_df = tic.history(period="5y")
        aapl_df['Close'].plot(title="APPLE's stock price")
        plt.show()
        
