import yfinance as yf

# Download historical data for VWO - pick any range you want
ticker = ['AAPL', 'VTV', 'VUG', 'VIOV']
data = yf.download(
    ticker, 
    start="2019-09-03", 
    end="2019-10-01", 
    auto_adjust=True
)["Close"]  # up to roughly today


# The 'Adj Close' column is what we want - fully adjusted for splits + dividends
print("Recent adjusted closes from yfinance:")
print(data['Close'].tail(10))  # last 10 trading days

# Or grab a specific date - example: March 9, 2026
specific_date = "2019-09-03"
if specific_date in data.index:
    adj_close = data.loc[specific_date, 'Close']
    print(f"\nAdjusted Close for {ticker} on {specific_date}: {adj_close[ticker]:.4f}")
else:
    print(f"No data for {specific_date} - maybe a weekend/holiday?")

# Bonus: compare Adj Close vs Close on a known dividend period (e.g. around Dec 2025 ex-div)
#print("\nExample comparison around a dividend date:")
#print(data[['Close', 'Adj Close']].loc['2025-12-15':'2025-12-20'])