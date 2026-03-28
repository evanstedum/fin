import yfinance as yf
import duckdb
import pandas as pd
from pathlib import Path
#if (not db_path.exists()) or (db_path.exists()):  # i.e. run this every time

cache_dir = Path.home() / ".cache" / "finance_data"
cache_dir.mkdir(parents=True, exist_ok=True)
db_path = cache_dir / "finance.duckdb"

tickers = ["AAPL", "MSFT", "GOOGL"]

if (not db_path.exists()) or (db_path.exists()):  # i.e. run this every time
    df = yf.download(tickers, auto_adjust=True, progress=False)
    df = df.stack(level=0).reset_index()
    df = df.rename(columns={"Price": "Type"})
    
    con = duckdb.connect(str(db_path))
    con.sql("CREATE OR REPLACE TABLE prices AS SELECT * FROM df")
    print("Downloaded and cached")
else:
    print("Using cache")

con = duckdb.connect(str(db_path))

dfx = con.sql("""
    SELECT Date, "AAPL", "GOOGL", "MSFT" 
    FROM prices 
    WHERE Type = 'Close'
    ORDER BY Date
""").df()

pass