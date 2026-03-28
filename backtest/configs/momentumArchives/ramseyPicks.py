""" 
ramseyPicks.py
2 of each from the below:
Growth
Growth and income
Aggressive growth
International
"""
import sys
from pathlib import Path
from datetime import date

from src.momentum import run_momentum

CONFIG = {
    "tickers_param": ["VUG", "QQQ", "VIG", "SCHD", "MGK", "IWY", "VXUS", "VEA"],
    "file_prefix": "ramseyPicks"
}

if __name__ == "__main__":
    run_momentum(**CONFIG)
