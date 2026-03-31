import requests
import pandas as pd

def fetch_ohlc(pair: str):
    url = "https://api.kraken.com/0/public/OHLC"
    params = {"pair": pair, "interval": 5}

    res = requests.get(url, params=params)
    data = res.json()

    result = data["result"]
    pair_key = [k for k in result.keys() if k != "last"][0]

    df = pd.DataFrame(result[pair_key], columns=[
        "time", "open", "high", "low", "close",
        "vwap", "volume", "count"
    ])

    df["close"] = df["close"].astype(float)
    return df
