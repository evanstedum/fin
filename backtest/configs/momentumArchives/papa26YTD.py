""" 
papaOrig.py
Papa bear original 13 
"""
import sys
from pathlib import Path
from datetime import date
# Make backtest/ the root for imports
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # parents[1] = backtest/
from src.momentum import run_momentum

CONFIG = {
    "tickers_param": [
        'VTV', 'VUG', 'VIOV', 'VIOG', 'VEA', 'VWO', 'VNQ',
        'PDBC', 'IAU', 'EDV', 'VGIT', 'VCLT', 'BNDX'
    ],
    "analysis_end": date.today().isoformat(),   # today
    "analysis_start": "2025-12-01",
    "fetch_start": "2024-10-01",  # ~14 months before analysis_start — safe buffer
    "file_prefix": "papa26YTD"
}


if __name__ == "__main__":
    run_momentum(**CONFIG)
