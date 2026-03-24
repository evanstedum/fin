""" 
200day.py

Bare bones 200day moving average demo
"""

import yfinance as yf
import pandas as pd

# Pick your ticker
ticker = "SPY"

# Download adjusted close prices for last 2 years
df = yf.download(ticker, period="2y", auto_adjust=True, progress=False)['Close']

# create mask based on 200-day SMA on adjusted close
mask = df > df.rolling(window=200).mean()


# Show last few rows with price + SMA
print(mask.tail(10))
pass
print("Done")