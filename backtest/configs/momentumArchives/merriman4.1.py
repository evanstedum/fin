""" 
merriman4.py
Merriman's 4 fund portfolio, with monthly rebalancing and independent bucket management 
"""
import sys
from pathlib import Path
from datetime import date

from src.momentum import run_momentum

CONFIG = {
    "tickers_param": ["VOO", "VONV", "VIOV", "VIOO"],
    "file_prefix": "merriman4"
}

if __name__ == "__main__":
    run_momentum(**CONFIG)
