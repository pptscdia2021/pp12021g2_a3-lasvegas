import yfinance as yf

Amazon = yf.Ticker("IBEX")
print(Amazon.info) 

print(Amazon.info['ask']) #Precio al que compro una acción
print(Amazon.info['bid']) #Precio al que vendo una acción

df = yf.download("IBEX", start="2021-09-03", end="2021-09-04",group_by="ticker") 
print(df)

ticker = yf.Ticker('IBEX')
aapl_df = ticker.history(period="5y")
aapl_df['Close'].plot(title="APPLE's stock price")