
import yfinance as yf
import pandas as pd
from yfcache import yfcache
from datetime import date

# Example script using yfcache class
cache = yfcache()

tickers=['AAPL', 'VIOV', 'VTV', 'VUG']
startd="2019-09-12"
endd="2019-12-31"

# Request adjusted close prices - will hit cache or download once
dfc = cache.get( tickers, startd, endd)

dfy = yf.download(tickers, start=startd, end=endd, auto_adjust=True, progress=False)["Close"]

iscached = (cache.iscached(tickers, startd, endd) != None).all().all() # check if every cell is cached

print(f"cached?{iscached}, same dfs?{dfc.equals(dfy)} Shape:{dfc.shape}, dfyShape:{dfy.shape} ")

print(dfy.head())
print("\nShape:", dfy.shape)
print("Index type:", type(dfy.index))
print("Columns:", dfy.columns.tolist())

tickers=['AAPL', 'VIOV', 'VTV', 'VUG']
start="2019-09-12"
end="2018-12-31"

df1 = cache.get(
    ticker_list=['AAPL', 'VIOV', 'VTV', 'VUG'],
    start_date="2019-09-10",
    end_date="2020-09-27"
)


# Subsequent calls with different date ranges reuse the same cache
df2 = cache.get(
    ticker_list=['AAPL', 'VIOV', 'VTV', 'VUG'],
    start_date="2019-09-10",
    end_date="2020-09-27"
)
df3 = cache.iscached(['AAPL', 'VUG'], start, end)

pass
print("\nSecond request shape:", df2.shape)