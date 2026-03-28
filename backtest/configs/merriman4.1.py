""" 
merriman4.py
Merriman's 4 fund portfolio, no rebalancing and independent bucket management 
"""
import sys
from pathlib import Path
from datetime import date
from backtest.src.momda import run_momda

CONFIG = {
    "tickers_param": ["VOO", "VONV", "VIOV", "VIOO"],
    "file_prefix": "merriNoBal",
    "rebalance_trigger": 1
}

if __name__ == "__main__":
    run_momda(**CONFIG)
