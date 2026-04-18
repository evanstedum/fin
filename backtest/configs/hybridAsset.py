""" 
grok19.py

Implements HAA: though not 100%  - but close. 
https://allocatesmartly.com/hybrid-asset-allocation/

"""

from backtest.src.momda import run_momda

CONFIG = {
    "tickers_param": [
        # US Equities (now full size spectrum + blend)
        "SPY",  # US large caps
        "IWM",  # US small caps
        "EFA",  # developed international stocks
        "EEM",  # emerging market stocks
        "VNQ",  # US real estate
        "PDBC", # commodities
        "IEF",  # intermediate-term US Treasuries
        "TLT",  # long-term US Treasuries
    ],
    "mda_param": 200,
    "top_assets": 4,
    "rebalance_trigger": 0,  # rebalance every month
    "mom_days": [21, 63, 126, 252], # 1, 3, 6, and 12 months in trading days (approx)
    "cash_etf": "TIP", # US Treasury Inflation-Protected Securities
    "file_prefix": "HybridAsset",
}


if __name__ == "__main__":
    run_momda(**CONFIG)
