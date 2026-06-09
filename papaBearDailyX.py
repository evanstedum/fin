"""
Papa Bear Daily Momentum Snapshot (Xtended version)

forked from momentumDaily

pulls last 7 days with momentum calcs.

"""
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import date, datetime, timedelta
import sys
from dateutil.relativedelta import relativedelta
from yfcache import yfcache


# ────────────────────────────────────────────────
# CONFIG
# ────────────────────────────────────────────────

tickers = [
    'VTV', 'VUG', 'VIOV', 'VIOG', 'VEA', 'VWO', 'VNQ',
    'PDBC', 'IAU', 'EDV', 'VGIT', 'VCLT', 'BNDX'
]

# Analysis period — get the last 7 days
now_et = pd.Timestamp.now(tz='US/Eastern')
is_today_bus_day = len(pd.bdate_range(now_et.date(), now_et.date())) > 0
market_closed = now_et.hour >= 16

if is_today_bus_day and market_closed:
    default_end_dt = now_et.date()
else:
    default_end_dt = (now_et.date() - pd.offsets.BusinessDay(1)).date()

default_end_str = default_end_dt.strftime("%Y-%m-%d")
user_input = input(f"Enter target date (YYYY-MM-DD) [default: {default_end_str}]: ").strip()
target_date_str = user_input if user_input else default_end_str
try:
    target_dt = pd.to_datetime(target_date_str)
except Exception:
    print(f"Error: Invalid date format entered: '{target_date_str}'. Please use YYYY-MM-DD.")
    sys.exit(1)

if target_dt.date() == now_et.date() and now_et.hour < 16:
    print(f"Error: Market is still open for {target_date_str}. Please run after 4:00 PM ET.")
    sys.exit(1)
elif target_dt.date() > now_et.date():
    print(f"Error: Cannot specify a future date: {target_date_str}.")
    sys.exit(1)

end_date_date = target_dt
end_date = target_dt.strftime("%Y-%m-%d")
start_date = (target_dt - pd.offsets.BusinessDay(5)).strftime("%Y-%m-%d")

# Fetch extra history so 252-day lookback works from day 1
fetch_start = (target_dt - relativedelta(months=14)).strftime("%Y-%m-%d")

# Lookback periods in trading days
periods = [63, 126, 252]
period_names = ['63', '126', '252']

# ← output files uses coded version of end date for easy tracking
output_file = f'/Users/evste/Downloads/csv/papabear{end_date_date.strftime("%Y%m%d")}-{datetime.now().strftime("%H%M")}.csv'

# ────────────────────────────────────────────────
# DOWNLOAD DATA
# ────────────────────────────────────────────────

print("Getting ticker adjusted close (auto_adjust=True)...")

cache = yfcache() # initialize caching
adj_close = cache.get (
    ticker_list=tickers,
    start_date=fetch_start,
    end_date=end_date,
    skip_cache=True # the daily papa gets latest data
).final_df

# Validate that the target date has market data
if target_dt not in adj_close.index:
    print(f"Cannot create the CSV for {target_date_str} because the market wasn't open.")
    sys.exit(0)

# ────────────────────────────────────────────────
# Prepare trading calendar
# ────────────────────────────────────────────────

trading_dates = adj_close.index.sort_values()
trading_dates = trading_dates[trading_dates >= pd.to_datetime(start_date)]
trading_dates = trading_dates[trading_dates <= pd.to_datetime(end_date)]

# print(f"Found {len(trading_dates)} trading days in range")

# ────────────────────────────────────────────────
# Calculate momentum rows — now for EVERY trading day
# ────────────────────────────────────────────────

rows = []

for as_of_date in trading_dates:           # ← changed from monthly_ends
    for ticker in tickers:
        if ticker not in adj_close.columns:
            continue

        try:
            current_close = adj_close.loc[as_of_date, ticker]
            if pd.isna(current_close):
                if as_of_date == target_dt:
                    print(f"DEBUG: Skipping {ticker} on {as_of_date.date()} - Today's Close is NaN")
                continue

            idx = adj_close.index.get_loc(as_of_date)
            past_dates  = []
            past_closes = []
            gains       = []

            for days_back in periods:
                if idx < days_back:
                    continue   # not enough history — skip this period (or you could skip whole row)

                past_idx = idx - days_back
                past_date = adj_close.index[past_idx]
                past_close = adj_close.iloc[past_idx][ticker]

                if pd.isna(past_close):
                    if as_of_date == target_dt:
                        print(f"DEBUG: Skipping {ticker} - Missing lookback data for {days_back} days ago ({past_date.date()})")
                    continue

                gain_pct = (current_close - past_close) / past_close * 100

                past_dates.append(past_date)
                past_closes.append(past_close)
                gains.append(gain_pct)

            # Only create row if we have at least some periods
            if not gains:
                continue

            papa_avg = np.mean(gains) # average of whatever periods we calculated
            
            # Serenity Ratio: Papa Avg / Std Dev of individual momentum components
            std_gains = np.std(gains)
            serenity_ratio = papa_avg / std_gains if std_gains != 0 else np.nan

            row = {
                'Symbol': ticker,
                'As of Date': as_of_date,
                'Close': round(float(current_close), 2),
                'Papa Avg': papa_avg,
                'Serenity Ratio': serenity_ratio,
            }

            for i, name in enumerate(period_names):
                # Only add columns for periods we actually calculated
                if i < len(past_dates):
                    row[name]                = past_dates[i].strftime('%m/%d/%Y')
                    row[f'{name} Day Close'] = round(float(past_closes[i]), 2)
                    row[f'{name} day gain']  = gains[i]

            rows.append(row)

        except (KeyError, ValueError) as e:
            continue

# ────────────────────────────────────────────────
# Build, sort, format and save
# ────────────────────────────────────────────────

if not rows:
    print("No valid rows generated — check data availability")
else:
    df = pd.DataFrame(rows)

    # Sort: newest date first, then highest Papa Avg within date
    df = df.sort_values(['As of Date', 'Papa Avg'], ascending=[False, False])

    # Calculate Z-Score (cross-sectional) for each date
    df['Z-Score'] = df.groupby('As of Date')['Papa Avg'].transform(lambda x: (x - x.mean()) / x.std()).round(2)

    # Format for readability
    df['As of Date'] = df['As of Date'].dt.strftime('%m/%d/%Y')
    for col in ['Papa Avg'] + [f'{p} day gain' for p in period_names]:
        # Only format columns that exist
        if col in df.columns:
            df[col] = df[col].round(2).astype(str) + '%'

    if 'Serenity Ratio' in df.columns:
        df['Serenity Ratio'] = df['Serenity Ratio'].round(2)

    # Reorder columns (only include ones that actually exist)
    cols_order = ['Symbol', 'As of Date', 'Close', 'Papa Avg', 'Z-Score']
    for p in period_names:
        if p in df.columns:
            cols_order += [p, f'{p} Day Close', f'{p} day gain']
            
    if 'Serenity Ratio' in df.columns:
        cols_order.append('Serenity Ratio')

    df = df[cols_order]

#    df.to_csv(output_file, index=False)
#    print(f"\nSaved {len(df)} rows to {output_file}")

    # Strictly filter for the user's requested target date to avoid showing "Yesterday" rows
    target_fmt = target_dt.strftime('%m/%d/%Y')
    latest_df = df[df['As of Date'] == target_fmt]

    print(
    latest_df
      [['Symbol', 'As of Date', 'Close', 'Papa Avg', 'Z-Score', 'Serenity Ratio']]
      .head(len(tickers)) # show all tickers only for the most recent date
    )


    latest_df[['Symbol', 'As of Date', 'Close', 'Papa Avg', 'Z-Score', 'Serenity Ratio']].head(len(tickers)).to_csv(output_file, index=False) # save this snippet to csv 

print(f"\nSaved {len(tickers)} rows to {output_file}")
