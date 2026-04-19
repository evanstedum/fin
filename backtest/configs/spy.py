""" 
spy.py
SPY only portfolio
"""
import sys
from pathlib import Path
from datetime import date

from backtest.src.momda import run_momda

CONFIG = {
    # avantis "tickers_param": ["AVUS", "AVLV", "AVSC", "AVUV"],
    "tickers_param": ["SPY"],
    # "mda_param": 200, EVS commented this out on (4/18/26) since MDA is not being used in this backtest
    # "  EVS commented this out on (4/18/26) since MDA is not being used in this backtest, and the file prefix is now just "spy"
    "file_prefix": "spy"
}

if __name__ == "__main__":
    run_momda(**CONFIG)
