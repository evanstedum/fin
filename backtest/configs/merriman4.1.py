""" 
merriman4.py
Merriman's 4 fund portfolio, with monthly rebalancing and independent bucket management 
"""
import sys
from pathlib import Path
from datetime import date
# Make backtest/ the root for imports
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # parents[1] = backtest/
from src.momda import run_momda

CONFIG = {
    "tickers_param": ["VOO", "VONV", "VIOV", "VIOO"],
    "file_prefix": "merriman4L"
}

if __name__ == "__main__":
    run_momda(**CONFIG)
