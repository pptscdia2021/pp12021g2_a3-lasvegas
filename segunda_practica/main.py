from web_scraping_bolsa import scraping
from Objetivo2 import maxYMin
from scrap_yahoo_finance import scrapYahoo
from comparativa import comparativa
from grafik import plotes


if __name__ == "__main__":
    df1 = scraping()
    df2 = scrapYahoo(df1['Ticker'])
    print(df1)
    print(df2)
    plotes(df1)