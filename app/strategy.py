def moving_average_signal(df, short_window, long_window):
    if len(df) < long_window:
        return "HOLD"

    short_ma = df["close"].rolling(short_window).mean()
    long_ma = df["close"].rolling(long_window).mean()

    if short_ma.iloc[-1] > long_ma.iloc[-1]:
        return "BUY"
    elif short_ma.iloc[-1] < long_ma.iloc[-1]:
        return "SELL"
    return "HOLD"
