
import yfinance as yf
import pandas as pd
from yfcache import yfcache
from datetime import date

# Example script using yfcache class
cache = yfcache()


# Request adjusted close prices - will hit cache or download once
df3 = cache.get(
    ticker_list=['AAPL', 'VUG'],
    start_date="2019-09-12",
    end_date="2018-12-31"
)

df = cache.get(
    ticker_list=['AAPL', 'VIOV', 'VTV', 'VUG'],
    start_date="2019-09-12",
    end_date="2018-12-31"
)

print(df.head())
print("\nShape:", df.shape)
print("Index type:", type(df.index))
print("Columns:", df.columns.tolist())

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