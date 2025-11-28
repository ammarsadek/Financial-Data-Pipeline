import pandas as pd

def add_indicators(df):
    df = df.sort_values("date")

    df['returns'] = df["close"].pct_change()

    df["volatility_30"] = df["returns"].rolling(30).std()
    df["volatility_60"] = df["returns"].rolling(60).std()

    df["ma-20"] = df["close"].rolling(20).mean()
    df["ma-50"] = df["close"].rolling(50).mean()
    df["ma_200"] = df["close"].rolling(200).mean()

    df["ema_20"] =df["close"].ewm(span=20, adjust=False).mean()
    df["ema_50"] = df["close"].ewm(span=50, adjust=False).mean()

    return df
