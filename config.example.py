# Copy to config.py or load from environment variables.
# NEVER commit real keys.

HYPERLIQUID_PRIVATE_KEY = "0xyour_private_key_here"
HYPERLIQUID_WALLET_ADDRESS = "0xyour_wallet_address_here"

# Risk limits (hard-coded in the bot)
MAX_LEVERAGE = 5          # start low
MAX_POSITION_PCT = 0.02   # 2% of equity per trade
MAX_DAILY_LOSS_PCT = 0.05 # 5% daily loss limit
SYMBOL = "BTC/USDC:USDC"  # Hyperliquid BTC perpetual
