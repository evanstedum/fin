""" 
equityMomentum.py

AI generated list of etf using momentum strategy.

"""
import sys
from pathlib import Path
from datetime import date
from backtest.src.momda import run_momda

CONFIG = {
    "tickers_param": [
        'MTUM',    #iShares MSCI USA Momentum
        'SPMO',    #Invesco S&P 500 Momentum
        'JMOM',    #JPMorgan U.S. Momentum
        'QMOM',    #Alpha Architect Quant Momentum
        'FMTM',    #MarketDesk Focused Momentum
        'PDP',     #Invesco Dorsey Wright Momentum
        'RFG',     #Invesco S&P MidCap 400 Growth
        'DWAS',    #Invesco DWA SmallCap Leaders
        'VFMO',    #Vanguard U.S. Momentum
        'ALTL',    #Pacer Lunt Large Cap Alternator 
    ],
    "mda_param": 200,
    "top_assets": 5,
    # "rebalance_trigger": 1.0,
    "file_prefix": "equityMomentumMdaV2"
}


if __name__ == "__main__":
    run_momda(**CONFIG)
