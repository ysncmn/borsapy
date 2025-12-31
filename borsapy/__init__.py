"""
borsapy - Turkish Financial Markets Data Library

A yfinance-like API for BIST stocks, forex, crypto, funds, and economic data.

Examples:
    >>> import borsapy as bp

    # Get stock data
    >>> stock = bp.Ticker("THYAO")
    >>> stock.info  # Real-time quote
    >>> stock.history(period="1mo")  # OHLCV data
    >>> stock.balance_sheet  # Financial statements

    # Get forex/commodity data (coming soon)
    >>> usd = bp.FX("USD")
    >>> gold = bp.FX("gram-altin")

    # Get crypto data (coming soon)
    >>> btc = bp.Crypto("BTCTRY")

    # Get fund data (coming soon)
    >>> fund = bp.Fund("AAK")

    # Get inflation data (coming soon)
    >>> inflation = bp.Inflation()
"""

from borsapy.ticker import Ticker
from borsapy.exceptions import (
    BorsapyError,
    TickerNotFoundError,
    DataNotAvailableError,
    APIError,
    AuthenticationError,
    RateLimitError,
    InvalidPeriodError,
    InvalidIntervalError,
)

__version__ = "0.1.0"
__author__ = "Said Surucu"

__all__ = [
    # Main classes
    "Ticker",
    # Exceptions
    "BorsapyError",
    "TickerNotFoundError",
    "DataNotAvailableError",
    "APIError",
    "AuthenticationError",
    "RateLimitError",
    "InvalidPeriodError",
    "InvalidIntervalError",
]
