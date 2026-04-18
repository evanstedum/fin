""" 
papaOrig.py
Papa bear original 13 
"""
import sys
from pathlib import Path
from datetime import date

from backtest.src.momda import run_momda

CONFIG = {
    "tickers_param": [
        'VTV', 'VUG', 'VIOV', 'VIOG', 'VEA', 'VWO', 'VNQ',
        'PDBC', 'IAU', 'EDV', 'VGIT', 'VCLT', 'BNDX'
    ],
    "mda_param": 200,
    "cash_etf": "TIP",
    "file_prefix": "papaOrigMdaTip"
}


if __name__ == "__main__":
    run_momda(**CONFIG)
