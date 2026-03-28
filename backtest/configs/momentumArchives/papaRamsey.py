""" 
pappapaRamseyaOrig.py
Papa bear original 13 plus Dave Ramsey's 8 picks, 
"""
import sys
from pathlib import Path
from datetime import date

from src.momentum import run_momentum

CONFIG = {
    "tickers_param": [
        'VTV', 'VUG', 'VIOV', 'VIOG', 'VEA', 'VWO', 'VNQ',
        'PDBC', 'IAU', 'EDV', 'VGIT', 'VCLT', 'BNDX', "QQQ", "VIG", "SCHD", "MGK", "IWY", "VXUS"
    ],
    "file_prefix": "PapaRamsey"
}


if __name__ == "__main__":
    run_momentum(**CONFIG)
