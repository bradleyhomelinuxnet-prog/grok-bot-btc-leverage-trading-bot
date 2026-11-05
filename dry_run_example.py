"""Minimal Hyperliquid BTC perpetual dry-run example.
Fetches market data. Places NO real orders.
"""
import os
import ccxt
from dotenv import load_dotenv

load_dotenv()

private_key = os.getenv("HYPERLIQUID_PRIVATE_KEY", "")
wallet_address = os.getenv("HYPERLIQUID_WALLET_ADDRESS", "")

exchange = ccxt.hyperliquid({
    "privateKey": private_key,
    "walletAddress": wallet_address,
    "enableRateLimit": True,
})

symbol = "BTC/USDC:USDC"

print("Loading markets...")
exchange.load_markets()

ticker = exchange.fetch_ticker(symbol)
print(f"Ticker {symbol}: last={ticker['last']}")

print("\nDry-run complete. No orders placed.")
print("Public market data is working.")
