"""Minimal Hyperliquid BTC perpetual dry-run example.
Fetches market data and balance. Places NO real orders.
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

# Optional: use testnet if you want
# exchange.set_sandbox_mode(True)

symbol = "BTC/USDC:USDC"

print("Loading markets...")
exchange.load_markets()

ticker = exchange.fetch_ticker(symbol)
print(f"Ticker {symbol}: last={ticker['last']}")

if private_key and wallet_address:
    balance = exchange.fetch_balance()
    print("Balance:", balance.get("USDC", {}))
else:
    print("No credentials set — skipping private endpoints (dry-run safe)")

print("\nDry-run complete. No orders placed.")
print("Next: implement strategy logic with hard risk limits before any live trading.")
