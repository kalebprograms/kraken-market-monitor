# kraken-market-monitor

Python-based market monitoring and paper trading system using Kraken API, rule-based strategy logic, risk controls, and trade logging.

## Overview

This project demonstrates a modular Python system that integrates with the Kraken API to monitor real-time market data, generate trading signals, and simulate trade execution using configurable logic.

The goal of this project is to showcase practical software engineering skills including API integration, data processing, automation, and clean project structure.

## Features

* Fetches live OHLC market data from Kraken API
* Generates trading signals using moving average strategy
* Modular Python architecture (separated logic for API, strategy, execution)
* Paper trading simulation (no real trades)
* Easily configurable for different pairs and strategies

## Project Structure

```
kraken-market-monitor/
├── app/
│   ├── main.py
│   ├── kraken_client.py
│   ├── strategy.py
├── tests/
├── requirements.txt
├── README.md
```

## How It Works

1. Fetch OHLC data from Kraken API
2. Calculate moving averages
3. Generate BUY, SELL, or HOLD signal
4. Output decision

## Setup

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the project

```bash
python app/main.py
```

## Example Output

```bash
Signal: BUY
```

## Future Improvements

* Add risk management module
* Add logging and trade history storage
* Add backtesting functionality
* Add support for multiple trading strategies
* Add dashboard or API interface

## Disclaimer

This project is for educational and portfolio purposes only. Not intended for live trading.


