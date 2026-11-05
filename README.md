# grok-bot-btc-leverage-trading-bot

# Grok Bot BTC Leverage Trading Bot (Bybit)

**WARNING: Extremely high risk. Leverage trading Bitcoin can result in total loss of capital in minutes.**

Starter scaffolding for an overnight Grok Bot style system focused on Bitcoin perpetual futures on Bybit. Defaults to dry-run / paper mode. Do not go live until you have verified behavior over many sessions with real market conditions.

## Key rules
- Always start in dry-run. Never enable live trading until thoroughly tested.
- Hard-code maximum position size, maximum leverage, and maximum daily loss.
- Use API keys with **trade permission only** (no withdrawal rights).
- One service places orders. Always check order status before retrying.
- Never commit real API keys or secrets.

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
