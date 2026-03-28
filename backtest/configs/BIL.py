""" 
grok19.py
Grok's recommendation to expand the original 13 picks to 19,
https://grok.com/share/bGVnYWN5_83844bc9-d263-48e2-a614-05e4659f090a


"""
import sys
from pathlib import Path
from datetime import date

from backtest.src.momda import run_momda

CONFIG = {
    "tickers_param": [
        # US Equities (now full size spectrum + blend)
        "BIL",   # 1-3 month tbil
    ],
    "file_prefix": "tBill"
}


if __name__ == "__main__":
    run_momda(**CONFIG)
