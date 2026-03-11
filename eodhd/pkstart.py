"""
example_api.py

Examples of using the EODHD Python Financial Library (APIClient)
"""

import config as cfg
from eodhd import APIClient



if __name__ == "__main__":
    api = APIClient(cfg.API_KEY)

    # --- Intraday / Historical ---
#    resp1 = api.get_intraday_historical_data("BTC-USD.CC", "1m")
    # print(resp)

#    resp2 = api.get_historical_data("BTC-USD.CC", "5m")
    # print(resp)

#    resp3 = api.get_historical_data("BTC-USD.CC", "1h")
    # print(resp)

#    resp4 = api.get_historical_data("BTC-USD.CC", "d")
    # print(resp)

#    resp5 = api.get_historical_data("BTC-USD.CC", "d", results=400)
    # print(resp)

#    resp5 = api.get_historical_data("AAPL.US", "d", results=100)

    # --- Lists / symbol change history ---
#    resp = api.get_list_of_exchanges()
#    print(resp)

#    resp = api.get_list_of_tickers(delisted=1, code="US")
#    print(resp)



    # --- EOD historical stock market data ---
    resp6 = api.get_eod_historical_stock_market_data(
        symbol="AAPL.US",
        period="d",
        from_date="2023-01-01",
        to_date="2023-01-03",
        order="a",
    )

    print("hello")
#    print(resp)



