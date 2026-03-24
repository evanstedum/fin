# Assuming df has Date index and columns of tickers
# and you want to append n identical copies of 'AAPL' columns
import pandas as pd
import yfinance as yf
import numpy as np

ticker = 'AAPL'
n = 3

data = yf.download(ticker, auto_adjust=True)['Close']

new_cols = [f"{ticker}_{i+1}" for i in range(n)]

df = pd.DataFrame(index=data.index)
df = df.assign(**{col: data for col in new_cols})

pass 
#df[new_cols] = pd.DataFrame(
#    data.values[:, None].repeat(n, axis=1),
#    index=data.index,
#    columns=new_cols
# )



pass