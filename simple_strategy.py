"""Simple Hyperliquid BTC perpetual strategy loop (DRY-RUN ONLY).
No real orders are placed.
"""
import os
import time
import ccxt
from dotenv import load_dotenv

load_dotenv()

# --- Risk limits (edit these) ---
MAX_LEVERAGE = 5
MAX_POSITION_PCT = 0.02   # 2% of equity per trade
MAX_DAILY_LOSS_PCT = 0.05 # 5% daily loss limit
SYMBOL = "BTC/USDC:USDC"
CHECK_INTERVAL = 60       # seconds between checks

private_key = os.getenv("HYPERLIQUID_PRIVATE_KEY", "")
wallet_address = os.getenv("HYPERLIQUID_WALLET_ADDRESS", "")

exchange = ccxt.hyperliquid({
    "privateKey": private_key,
    "walletAddress": wallet_address,
    "enableRateLimit": True,
})

def get_ticker():
    ticker = exchange.fetch_ticker(SYMBOL)
    return ticker["last"]

def simple_signal(price):
    """Placeholder signal. Replace with real logic later."""
    # Example: very basic momentum dummy
    # For now it just returns "hold"
    return "hold"

def main():
    print("Starting dry-run strategy loop...")
    print(f"Symbol: {SYMBOL}")
    print(f"Max leverage: {MAX_LEVERAGE}x")
    print(f"Max position: {MAX_POSITION_PCT*100}% of equity")
    print(f"Max daily loss: {MAX_DAILY_LOSS_PCT*100}%")
    print("No real orders will be placed.\n")

    while True:
        try:
            price = get_ticker()
            signal = simple_signal(price)
            print(f"[{time.strftime('%H:%M:%S')}] Price: {price} | Signal: {signal}")

            # --- Future place for risk checks and order logic ---
            # if signal == "long" and risk_ok():
            #     size = calculate_size(...)
            #     # exchange.create_order(...)  <-- still commented out

        except Exception as e:
            print(f"Error: {e}")

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
