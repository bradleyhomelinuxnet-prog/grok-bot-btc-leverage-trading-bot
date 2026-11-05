# Copy to config.py or load from environment variables.
# NEVER commit real keys.

BYBIT_API_KEY = "your_api_key_here"
BYBIT_SECRET = "your_secret_here"

# Risk limits (hard-coded in the bot)
MAX_LEVERAGE = 5          # start low
MAX_POSITION_PCT = 0.02   # 2% of equity per trade
MAX_DAILY_LOSS_PCT = 0.05 # 5% daily loss limit
SYMBOL = "BTC/USDT:USDT"  # Bybit linear perpetual
