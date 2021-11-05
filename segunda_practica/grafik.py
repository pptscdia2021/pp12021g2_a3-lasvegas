import matplotlib.pyplot as plt
import yfinance as yf

def plotes(df):
    tiko = df['Ticker']
    i = 0
    while i < 2:
        tic = yf.Ticker(tiko[i])
        dibuDf = tic.history(period = "5y")
        dibuDf['Close'].plot(title = tiko[i])
        i = i + 1
        plt.show()