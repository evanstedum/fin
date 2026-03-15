""" 
merriman4.py
Papa bear 13 + Merriman's 4 fund portfolio, with monthly rebalancing and independent bucket management 
"""
import sys
from pathlib import Path
from datetime import date
# Make backtest/ the root for imports
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # parents[1] = backtest/
from src.momentum import run_momentum

CONFIG = {
    # avantis "tickers_param": ["AVUS", "AVLV", "AVSC", "AVUV"],
    "tickers_param": ["VOO", "VONV", "VIOV", "VIOO"],
    "analysis_start": "2016-01-01",
    "analysis_end":   date.today().isoformat(),   # today
    "fetch_start": "2015-01-01",
    "file_suffix_param": "plusMerrim",
    "output_dir_param": "/Users/peterkay/Downloads/backtestFiles"
}

if __name__ == "__main__":
    run_momentum(**CONFIG)
