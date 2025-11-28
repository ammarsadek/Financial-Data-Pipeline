import requests
import pandas as pd
from config import API_KEY, BASE_URL

def fetch_stock_data(symbol):
    url = f"{BASE_URL}function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"HTTP error for {symbol}: {response.status_code}")

    data = response.json()

    if "Time Series (Daily)" not in data:
        raise Exception(f"AlphaVantage returned no daily data for {symbol}: {data}")

    ts = data["Time Series (Daily)"]

    df = pd.DataFrame.from_dict(ts, orient='index')
    df.reset_index(inplace=True)
    df.rename(columns={
        "index": "date",
        "1. open": "open",
        "2. high": "high",
        "3. low": "low",
        "4. close": "close",
        "5. volume": "volume",
    }, inplace=True)

    return df

def fetch_all_stock_data(symbols):
    all_data = {}
    for s in symbols:
        print(f"Fetching {s} from AlphaVantage... ")
        df = fetch_stock_data(s)
        all_data[s] = df
    return all_data

