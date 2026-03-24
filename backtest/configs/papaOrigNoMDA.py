""" 
papaOrigNoMDA.py
runs the mda code but doesn't do mda - should exactly match papaOrigL files.
"""
import sys
from pathlib import Path
from datetime import date
# Make backtest/ the root for imports
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # parents[1] = backtest/
from src.momda import run_momda


CONFIG = {
    "tickers_param": [
        'VTV', 'VUG', 'VIOV', 'VIOG', 'VEA', 'VWO', 'VNQ',
        'PDBC', 'IAU', 'EDV', 'VGIT', 'VCLT', 'BNDX'
    ],
    "file_prefix": "papaNoMDA"
}


if __name__ == "__main__":
    run_momda(**CONFIG)
