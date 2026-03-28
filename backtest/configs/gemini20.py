""" 
gemini20.py
NotebookLM's recommendation to expand the original 13 picks to 20,


"""
import sys
from pathlib import Path
from datetime import date

from backtest.src.momda import run_momda

CONFIG = {
    "tickers_param": [
        # US Equities
        'VV',    # US Large Cap Blend
        'MTUM',  # US Large Cap Momentum
        'IJH',   # US Mid Cap
        'VIOO',  # US Small Cap Blend
        'IWC',   # US Micro-Cap
        
        # International & Emerging Equities
        'VEA',   # International Developed Blend
        'VWO',   # Emerging Markets
        'VSS',   # International Small Cap Blend
        'EWX',   # Emerging Markets Small Cap
        
        # Real Assets & Alternatives
        'VNQ',   # US REITs
        'VNQI',  # International REITs
        'DBC',   # Broad Commodities
        'IAU',   # Gold
        'TREE',  # Timber
        
        # Fixed Income
        'VGIT',  # Intermediate-Term US Treasuries
        'TLT',   # Long-Term US Treasuries
        'VTIP',  # Treasury Inflation-Protected Securities (TIPS)
        'LQD',   # US Corporate Bonds (Investment Grade)
        'HYG',   # US High Yield Credit (Junk Bonds)
        'BNDX',  # Non-US Developed Bonds
        'VWOB'   # Emerging Market Bonds
    ],
    "mda_param": 200,
    "top_assets": 5,
    "file_prefix": "Gemini5Mda"
}


if __name__ == "__main__":
    run_momda(**CONFIG)
