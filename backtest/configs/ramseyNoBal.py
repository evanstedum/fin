""" 
ramseyNoBal.py

don't momentum balance

"""
import sys
from pathlib import Path
from datetime import date

from backtest.src.momda import run_momda

CONFIG = {
    "tickers_param": ["VUG", "QQQ", "VIG", "SCHD", "MGK", "IWY", "VXUS", "VEA"],
    "file_prefix": "ramseyNoBal",
    "rebalance_trigger": 1
}

if __name__ == "__main__":
    run_momda(**CONFIG)
