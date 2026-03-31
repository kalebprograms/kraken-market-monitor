from app.kraken_client import fetch_ohlc
from app.strategy import moving_average_signal

def main():
    df = fetch_ohlc("XXBTZUSD")
    signal = moving_average_signal(df, 5, 20)
    print(f"Signal: {signal}")

if __name__ == "__main__":
    main()
