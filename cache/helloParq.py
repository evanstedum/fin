import yfinance as yf
import pandas as pd
from pathlib import Path

cache_dir = Path.home() / ".cache" / "finance_data"
cache_dir.mkdir(parents=True, exist_ok=True)

ticker = "AAPL"
parquet_path = cache_dir / f"{ticker}.parquet"

# Download if not cached
if not parquet_path.exists():
    df = yf.download(ticker, auto_adjust=True, progress=False)
    df.to_parquet(parquet_path)
    print("Downloaded and cached")
else:
    print("Using cache")

# Read back
df = pd.read_parquet(parquet_path)
print(df.tail())