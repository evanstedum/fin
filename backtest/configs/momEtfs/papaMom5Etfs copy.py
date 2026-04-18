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
    'GMOM',
]

CONFIG = {
    "tickers_param": momentum_etfs,
    # "mda_param": 200,
    # "top_assets": 3,
    "rebalance_trigger": 1.0,
    "file_prefix": "metaMom3NoBal"
}


if __name__ == "__main__":
    run_momda(**CONFIG)
