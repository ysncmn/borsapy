# borsapy

Turkish financial markets data library - yfinance-like API for BIST stocks, forex, crypto, and more.

## Installation

```bash
pip install borsapy
```

## Quick Start

```python
import borsapy as bp

# Get stock data
stock = bp.Ticker("THYAO")

# Real-time quote
print(stock.info)

# Historical OHLCV data
df = stock.history(period="1mo")
print(df)

# Financial statements
print(stock.balance_sheet)
print(stock.income_stmt)
print(stock.cashflow)
```

## Features

- **Stock Data**: Real-time quotes and historical OHLCV from Turkish sources
- **Financial Statements**: Balance sheet, income statement, cash flow
- **Coming Soon**: Forex, commodities, crypto, mutual funds, inflation data

## Data Sources

- İş Yatırım (real-time quotes, financial statements)
- Paratic (historical OHLCV)
- doviz.com (forex, commodities)
- BtcTurk (crypto)
- TEFAS (mutual funds)
- TCMB (inflation)

## License

MIT
