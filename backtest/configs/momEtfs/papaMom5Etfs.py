""" 
papaMom5Etfs.py

Momentum etf equivalents to the original papa bear 13.
Rotating on top 5. 

"""
import sys
from pathlib import Path
from datetime import date
from backtest.src.momda import run_momda

momentum_etfs = [
    'MTUM',    # iShares MSCI USA Momentum
    'SPMO',    # Invesco S&P 500 Momentum
    'QMOM',    # Alpha Architect US Quantitative Momentum
    'PDP',     # Invesco Dorsey Wright Momentum
    'XSVM',    # Invesco S&P SmallCap Value with Momentum
    'DWAS',    # Invesco Dorsey Wright SmallCap Momentum
    'QSML',    # Pacer Lunt SmallCap Multi-Factor Alternative
    'XSMO',    # Invesco S&P SmallCap Momentum
    'IMTM',    # iShares MSCI Intl Momentum Factor
    'IDMO',    # Invesco S&P International Developed Momentum
    'EEMO',    # iShares MSCI Emerging Markets Momentum
    'FRI',     # First Trust S&P REIT Index
    'PPTY',    # U.S. Diversified Real Estate
    'COM',     # Direxion Auspice Broad Commodity Strategy
    'BCI',     # Abrdn Bloomberg All Commodity Strategy
    'GYEN',    # WisdomTree Japan Hedged Equity (FX Momentum Proxy)
    'TMF',     # Direxion Daily 20+ Year Treasury Bull 3X
    'USTB',    # VictoryShares USAA Core Intermediate Bond (Active/Momentum)
    'SYLD',    # Cambria Shareholder Yield (High Momentum Factor)
    'MINC',    # Ianis 0-5 Yr Fixed Income (Active Trend/Momentum)
    'IGIB',    # iShares 5-10 Year Investment Grade Corporate Bond
    'EMB'      # iShares J.P. Morgan USD Emerging Markets Bond (Liquid US version)
]

CONFIG = {
    "tickers_param": momentum_etfs,
    # "mda_param": 200,
    "top_assets": 5,
    # "rebalance_trigger": 1.0,
    "file_prefix": "papaMom5Etfs"
}


if __name__ == "__main__":
    run_momda(**CONFIG)
