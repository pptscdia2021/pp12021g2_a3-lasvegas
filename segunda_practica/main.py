from web_scraping_bolsa import scraping
from Objetivo2 import maxYMin
from scrap_yahoo_finance import scrapYahoo
from comparativa import comparativa

accionesYahoo = ["ANA.MC", "BBVA.MC", "GRF.MC", "ELE.MC","REP.MC"]

if __name__ == "__main__":
    df1 = scraping()
    df2 = scrapYahoo(accionesYahoo)
    comparativa(df1,df2)