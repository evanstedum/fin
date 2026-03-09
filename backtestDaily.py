# daily_momentum_backtester.py
# Daily momentum ETF rotation backtester with portfolio-level threshold rebalancing
# Ranks every trading day, holds top 3, keeps qty if ticker unchanged, else reinvests proceeds
# Triggers full portfolio rebalance if any bucket drifts > threshold from equal weight

import pandas as pd
import numpy as np
import yfinance as yf
from pathlib import Path

# ────────────────────────────────────────────────
#           CONFIGURATION
# ────────────────────────────────────────────────

TICKERS = [
    "VTV", "VUG", "VIOV", "VIOG", "VEA", "VWO", "VNQ",
    "PDBC", "IAU", "EDV", "VGIT", "VCLT", "BNDX"
]

analysis_start = "2007-10-31"   # inclusive
analysis_end   = "2008-01-30"   # exclusive

# Fetch extra history so 252-day lookback is valid from first analysis day
fetch_start    = "2006-08-01"   # ~13 months buffer before analysis_start

INITIAL_VALUE = 100_000
VALUE_PER_BUCKET = INITIAL_VALUE // 3

# Momentum lookbacks in **trading days**
PERIODS = [63, 126, 252]
PERIOD_NAMES = ["63", "126", "252"]  # only used if saving full history

REBALANCE_THRESHOLD = 0.20  # 20% drift → full rebalance

FILE_SUFFIX = "2007dailyRebalancing"

OUTPUT_DIR = Path("/Users/peterkay/Downloads/backtestFiles")
OUTPUT_DIR.mkdir(exist_ok=True)

# ────────────────────────────────────────────────
# 1. Download adjusted close prices
# ────────────────────────────────────────────────

print("Downloading adjusted close data...")
data = yf.download(
    tickers=TICKERS,
    start=fetch_start,
    end=analysis_end,
    auto_adjust=True,          # dividends & splits adjusted
    progress=True
)

# Extract adjusted Close
if "Close" in data.columns.levels[0]:
    adj_close = data["Close"]
else:
    raise ValueError("No 'Close' column found in downloaded data")

print(f"Downloaded shape: {adj_close.shape}")
print(f"Date range: {adj_close.index.min().date()} → {adj_close.index.max().date()}")

# Filter to analysis period
analysis_dates = adj_close.index[
    (adj_close.index >= pd.to_datetime(analysis_start)) &
    (adj_close.index < pd.to_datetime(analysis_end))
]

print(f"\n{len(analysis_dates)} trading days in analysis window")

# ────────────────────────────────────────────────
# 2. Daily backtest loop
# ────────────────────────────────────────────────

backtest_rows = []

prev_tickers = [None, None, None]
prev_qtys    = [0.0, 0.0, 0.0]   # use float so we don't lose pennies on rotation

min_lookback = max(PERIODS)  # 252

for as_of_date in analysis_dates:

    idx = adj_close.index.get_loc(as_of_date)

    if idx < min_lookback:
        continue  # not enough history yet

    # Compute momentum for all valid tickers today
    momentum_list = []

    for ticker in TICKERS:
        if ticker not in adj_close.columns:
            continue

        current_close = adj_close.loc[as_of_date, ticker]
        if pd.isna(current_close) or current_close <= 0:
            continue

        gains = []
        valid = True

        for days_back in PERIODS:
            past_idx = idx - days_back
            past_close = adj_close.iloc[past_idx][ticker]

            if pd.isna(past_close) or past_close <= 0:
                valid = False
                break

            gain_pct = (current_close / past_close - 1) * 100
            gains.append(gain_pct)

        if not valid:
            continue

        papa_avg = np.mean(gains)

        momentum_list.append({
            "Ticker": ticker,
            "Close": current_close,
            "Papa Avg": papa_avg
        })

    if len(momentum_list) < 3:
        print(f"Skipping {as_of_date.date()}: only {len(momentum_list)} valid tickers")
        continue

    # Rank → take top 3
    today_df = pd.DataFrame(momentum_list)
    today_df = today_df.sort_values("Papa Avg", ascending=False).head(3).reset_index(drop=True)

    curr_tickers = today_df["Ticker"].tolist()
    curr_closes  = today_df["Close"].tolist()

    # ── Position management per bucket ───────────────────────────
    qtys = [0.0, 0.0, 0.0]
    values = [0.0, 0.0, 0.0]

    for i in range(3):
        curr_ticker = curr_tickers[i]
        curr_close = curr_closes[i]

        if prev_tickers[i] is None:
            # First allocation
            qtys[i] = VALUE_PER_BUCKET / curr_close   # float qty ok for backtest
        elif curr_ticker == prev_tickers[i]:
            # Keep same position size
            qtys[i] = prev_qtys[i]
        else:
            # Sell old → buy new with full proceeds
            old_ticker = prev_tickers[i]
            old_close = adj_close.loc[as_of_date, old_ticker]

            if pd.isna(old_close) or old_close <= 0:
                proceeds = 0.0
            else:
                proceeds = prev_qtys[i] * old_close

            qtys[i] = proceeds / curr_close

    # Current market values after possible rotation
    for i in range(3):
        values[i] = qtys[i] * curr_closes[i]

    total = sum(values)

    # ── Check for portfolio drift & rebalance if needed ─────────
    if total > 0:
        target = total / 3
        needs_rebalance = False
        for val in values:
            if abs(val - target) / target > REBALANCE_THRESHOLD:
                needs_rebalance = True
                break

        if needs_rebalance:
            for i in range(3):
                qtys[i] = target / curr_closes[i]
            # Recalculate values after forced equal weighting
            for i in range(3):
                values[i] = qtys[i] * curr_closes[i]
            total = sum(values)

    # ── Record row ──────────────────────────────────────────────
    backtest_rows.append({
        "As of Date": as_of_date.strftime("%Y-%m-%d"),
        "B1 Ticker": curr_tickers[0],
        "B1 Qty": round(qtys[0], 4),     # more precision for daily
        "B1 Value": round(values[0]),
        "B2 Ticker": curr_tickers[1],
        "B2 Qty": round(qtys[1], 4),
        "B2 Value": round(values[1]),
        "B3 Ticker": curr_tickers[2],
        "B3 Qty": round(qtys[2], 4),
        "B3 Value": round(values[2]),
        "Total Value": round(total)
    })

    # Carry forward
    prev_tickers = curr_tickers
    prev_qtys = qtys

# ────────────────────────────────────────────────
# 3. Save results
# ────────────────────────────────────────────────

if not backtest_rows:
    print("No backtest rows generated — check data availability / lookback periods")
else:
    backtest_df = pd.DataFrame(backtest_rows)

    # Add $ formatting like your original
    for col in ["B1 Value", "B2 Value", "B3 Value", "Total Value"]:
        backtest_df[col] = backtest_df[col].apply(lambda x: f"${x:,.0f}" if pd.notna(x) else "")

    filename = f"dailyBacktestResults_{FILE_SUFFIX}.csv"
    backtest_df.to_csv(OUTPUT_DIR / filename, index=False)
    print(f"\nSaved {len(backtest_df)} rows to: {filename}")
    print("Folder:", OUTPUT_DIR.resolve())

print("\nDone!")