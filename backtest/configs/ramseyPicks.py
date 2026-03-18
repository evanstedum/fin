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
# Make backtest/ the root for imports
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # parents[1] = backtest/
from src.momentum import run_momentum

CONFIG = {
    "tickers_param": ["VUG", "QQQ", "VIG", "SCHD", "MGK", "IWY", "VXUS", "VEA"],
    "file_suffix_param": "ramseyPicks"
}

if __name__ == "__main__":
    run_momentum(**CONFIG)
