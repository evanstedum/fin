""" 
ramseyMDA.py
2 of each from the below:
Growth
Growth and income
Aggressive growth
International
includes the mda option
"""
import sys
from pathlib import Path
from datetime import date
# Make backtest/ the root for imports
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # parents[1] = backtest/
from src.momda import run_momda

CONFIG = {
    "tickers_param": ["VUG", "QQQ", "VIG", "SCHD", "MGK", "IWY", "VXUS", "VEA"],
    "mda_param": 200,
    "file_prefix": "ramseyMDA"
}

if __name__ == "__main__":
    run_momda(**CONFIG)
