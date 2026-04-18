""" 
ramseyPicks.py
2 of each from the below:
Growth
Growth and income
Aggressive growth
International

Momentum strategies involve buying securities that have had high recent returns and selling those that have had low recent returns, betting that the trend will continue.

Here are two ETFs for each of your requested asset classes that utilize momentum as a primary or significant strategy:

## 1. Growth
These funds target companies with strong earnings potential but refine their selection using price momentum to ensure they are catching stocks while they are "hot."
* **MTUM (iShares MSCI USA Momentum Factor ETF):** The gold standard for pure momentum. it selects large- and mid-cap U.S. stocks with the strongest price trends over the last 6–12 months.
* **PDP (Invesco Dorsey Wright Momentum ETF):** Uses a unique "relative strength" methodology to identify stocks that are outperforming their peers, regardless of their specific sector.

---

## 2. Growth and Income
These ETFs seek a "total return" approach, balancing the capital appreciation of momentum stocks with the safety of dividend payments or value-tilted growth.
* **SPVM (Invesco S&P 500 Value with Momentum ETF):** This fund targets the "sweet spot" of the S&P 500 by selecting stocks that show both attractive value characteristics and strong recent price momentum.
* **FDM (First Trust Dow Jones Select MicroCap Index Fund):** While primarily growth-oriented, this fund uses a multi-factor screen that includes relative price strength (momentum) alongside value and income-supporting metrics.

---

## 3. Aggressive Growth
Aggressive momentum funds often focus on smaller companies or high-beta sectors where price swings—and therefore momentum trends—are more extreme.
* **DWAS (Invesco Dorsey Wright SmallCap Momentum ETF):** This fund applies momentum screens specifically to the small-cap universe, which tends to be more volatile and potentially more rewarding during bull markets.
* **QMOM (Alpha Architect U.S. Quantitative Momentum ETF):** A "high-conviction" fund that uses a data-heavy quantitative model to find the stocks with the "purest" momentum, often leading to a more aggressive, concentrated portfolio.

---

## 4. International
These funds apply momentum screens to developed and emerging markets outside of the United States.
* **IMTM (iShares MSCI Intl Momentum Factor ETF):** Provides exposure to large- and mid-cap stocks in developed international markets (like Europe and Japan) that are exhibiting the highest price momentum.
* **PIE (Invesco Dorsey Wright Emerging Markets Momentum ETF):** Targets the highest relative strength stocks specifically within Emerging Markets, where momentum trends can be particularly powerful due to rapid economic shifts.

> **Note on Momentum:** Because momentum strategies rely on trends, these ETFs often have higher **turnover** (buying and selling stocks frequently) than standard index funds. This can lead to higher tax implications in taxable brokerage accounts.

Which of these asset classes are you looking to add to your portfolio first?

"""
import sys
from pathlib import Path
from datetime import date

from backtest.src.momda import run_momda

# List of Momentum ETFs by Asset Class
momentum_etfs = [
    "MTUM", "PDP",   # Growth
    "SPVM", "FDM",   # Growth and Income
    "DWAS", "QMOM",  # Aggressive Growth
    "IMTM", "PIE"    # International
]

CONFIG = {
    "tickers_param": momentum_etfs,
    "file_prefix": "ramseyMom"
}

if __name__ == "__main__":
    run_momda(**CONFIG)
