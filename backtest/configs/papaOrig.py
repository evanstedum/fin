""" 
papaOrig.py
Papa bear original 13 
"""
import sys
from pathlib import Path

# Add repo root to sys.path so we can import backtest modules
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from backtest.src.momda import run_momda

CONFIG = {
    "tickers_param": [
        'VTV', 'VUG', 'VIOV', 'VIOG', 'VEA', 'VWO', 'VNQ',
        'PDBC', 'IAU', 'EDV', 'VGIT', 'VCLT', 'BNDX'
    ],
    "file_prefix": "papaGEbal"
}


if __name__ == "__main__":
    run_momda(**CONFIG)
