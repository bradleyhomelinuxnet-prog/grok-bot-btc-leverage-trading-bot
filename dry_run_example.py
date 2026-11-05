"""Minimal Bybit BTC perpetual dry-run example.
Fetches market data and balance. Places NO real orders.
"""
import os
import ccxt
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("BYBIT_API_KEY", "")
secret = os.getenv("BYBIT_SECRET", "")

exchange = ccxt.bybit({
    "apiKey": api_key,
    "secret": secret,
    "options": {"defaultType": "swap"},  # perpetual futures
    "enableRateLimit": True,
})

exchange.set_sandbox_mode(True)  # Bybit testnet

symbol = "BTC/USDT:USDT"

print("Loading markets...")
exchange.load_markets()

ticker = exchange.fetch_ticker(symbol)
print(f"Ticker {symbol}: last={ticker['last']}")

if api_key:
    balance = exchange.fetch_balance()
    print("Balance (USDT):", balance.get("USDT", {}))
else:
    print("No API key set — skipping private endpoints (dry-run safe)")

print("\nDry-run complete. No orders placed.")
print("Next: implement strategy logic with hard risk limits before any live trading.")
