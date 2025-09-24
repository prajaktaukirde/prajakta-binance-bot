# Prajakta Ukirde - Binance Futures Order Bot (Example Submission)
## Project structure
prajakta-binance-bot/
├─ src/
│  ├─ logger.py
│  ├─ market_orders.py
│  ├─ limit_orders.py
│  └─ advanced/
│     ├─ oco.py
│     ├─ twap.py
│     └─ grid_strategy.py
├─ bot.log
├─ report.pdf
└─ README.md

## Requirements
- Python 3.8+
- (Optional) python-binance if you want to extend to live trading: `pip install python-binance`
- No API keys are stored in this example. If you want to enable live trading, set environment variables:
  - BINANCE_API_KEY
  - BINANCE_API_SECRET

## How to run (dry-run)
Examples:
- Market order (dry-run):
  `python src/market_orders.py BTCUSDT BUY 0.001 --dry`
- Limit order (dry-run):
  `python src/limit_orders.py BTCUSDT SELL 0.001 45000 --dry`
- TWAP (dry-run):
  ```python -c "from src.advanced.twap import execute_twap; execute_twap('BTCUSDT','BUY',0.01,intervals=4,interval_seconds=5,dry=True)"```

## Notes on safety & validation
- All example scripts default to **dry-run**. They validate symbol, side, quantity and price inputs.
- Live order placement is intentionally not implemented in this sample. Extend with `python-binance` and proper API key handling for live use.
- Logging is configured to write `bot.log` in the project root.

## What to include in the final submission (per assignment)
- A filled `report.pdf` with screenshots and explanation (placeholder included).
- Detailed README covering API setup and how to run scripts.
- Structured `bot.log` produced during your runs.

## License
MIT
