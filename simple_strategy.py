"""Simple Hyperliquid BTC perpetual strategy loop (DRY-RUN ONLY).
SMA crossover signal + position size calculator.
No real orders are placed.
"""
import os
import time
import ccxt
from dotenv import load_dotenv

load_dotenv()

# --- Risk limits ---
MAX_LEVERAGE = 5
MAX_POSITION_PCT = 0.02   # 2% of equity per trade
MAX_DAILY_LOSS_PCT = 0.05
SYMBOL = "BTC/USDC:USDC"
CHECK_INTERVAL = 60
SMA_PERIOD = 10

private_key = os.getenv("HYPERLIQUID_PRIVATE_KEY", "")
wallet_address = os.getenv("HYPERLIQUID_WALLET_ADDRESS", "")

exchange = ccxt.hyperliquid({
    "privateKey": private_key,
    "walletAddress": wallet_address,
    "enableRateLimit": True,
})

price_history = []

def get_ticker():
    ticker = exchange.fetch_ticker(SYMBOL)
    return ticker["last"]

def update_sma(price):
    price_history.append(price)
    if len(price_history) > SMA_PERIOD:
        price_history.pop(0)
    if len(price_history) < SMA_PERIOD:
        return None
    return sum(price_history) / len(price_history)

def simple_signal(price, sma):
    if sma is None:
        return "hold"
    if price > sma * 1.001:
        return "long"
    elif price < sma * 0.999:
        return "short"
    return "hold"

def calculate_size(price, equity=1000):
    risk_amount = equity * MAX_POSITION_PCT
    size_usd = risk_amount * MAX_LEVERAGE
    size_btc = size_usd / price
    return round(size_usd, 2), round(size_btc, 6)

def main():
    print("Starting dry-run strategy loop (SMA + size)...")
    print(f"Symbol: {SYMBOL}")
    print(f"Max leverage: {MAX_LEVERAGE}x")
    print(f"Max position: {MAX_POSITION_PCT*100}% of equity")
    print(f"SMA period: {SMA_PERIOD}")
    print("No real orders will be placed.\n")

    while True:
        try:
            price = get_ticker()
            sma = update_sma(price)
            signal = simple_signal(price, sma)
            size_usd, size_btc = calculate_size(price)

            sma_str = f"{sma:.1f}" if sma else "building..."
            print(f"[{time.strftime('%H:%M:%S')}] Price: {price} | SMA: {sma_str} | Signal: {signal} | Size: ${size_usd} (~{size_btc} BTC)")

        except Exception as e:
            print(f"Error: {e}")

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
