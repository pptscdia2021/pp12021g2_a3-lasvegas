from web_scraping_bolsa import scraping
from Objetivo2 import maxYMin
from scrap_yahoo_finance import scrapYahoo

accionesYahoo = ["ANA.MC", "BBVA.MC", "GRF.MC", "ELE.MC","REP.MC"]

if __name__ == "__main__":
    df1 = scraping()
    df2 = scrapYahoo(accionesYahoo)
    print(df1)
    print(df2)