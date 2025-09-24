# Prajakta Binance Bot

## Overview
This is a Python-based Binance Futures trading bot that supports **Market**, **Limit**, and **OCO (One Cancels Other)** orders.  
It includes basic order validation and logging. Optional advanced strategies like **TWAP** and **Grid** are also included.

## Features
- **Market Orders**: Instant buy/sell at market price.  
- **Limit Orders**: Buy/sell at a specific price.  
- **OCO Orders**: Combines take-profit and stop-limit in a single order.  
- **Logging**: All actions, errors, and dry-run outputs are logged to `bot.log`.  
- **Advanced Orders (Bonus)**: TWAP and Grid strategies implemented in `src/advanced/`.

## Folder Structure

prajakta-binance-bot/
│
├── src/
│ ├── market_orders.py # Market order logic
│ ├── limit_orders.py # Limit order logic
│ ├── validation.py # Order validation
│ ├── logger.py # Logging setup
│ ├── test_all_orders.py # Test all order types
│ └── advanced/
│ ├── oco.py # OCO order logic
│ ├── twap.py # TWAP strategy
│ └── grid_strategy.py # Grid strategy (optional)
│
├── bot.log # Logs for dry-run & API executions
├── README.md # Project documentation
└── report.pdf # Screenshots & explanations

bash
Copy code

## Setup

1. **Clone the repository**

```bash
git clone https://github.com/prajaktaukirde/prajakta-binance-bot.git
cd prajakta-binance-bot
Create a virtual environment and activate it

bash
Copy code
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux
Install dependencies

bash
Copy code
pip install -r requirements.txt
API Setup
Create a .env file in src/ with your Binance API keys:

ini
Copy code
API_KEY=your_binance_api_key
API_SECRET=your_binance_api_secret
How to Run
Test all orders in dry-run mode

bash
Copy code
python src/test_all_orders.py
Run individual orders

bash
Copy code
python src/market_orders.py BTCUSDT BUY 0.01
python src/limit_orders.py BTCUSDT SELL 0.01 45000
Advanced OCO order (dry-run)

python
Copy code
from advanced.oco import execute_oco

execute_oco(
    symbol="BTCUSDT",
    side="BUY",
    qty=0.001,
    stop_price=44000,
    stop_limit_price=43990,
    dry=True
)
Notes
Default mode is dry-run. Remove dry=True to place real trades.

Verify OCO take-profit and stop prices before executing live trades.

Logs are stored in src/bot.log with timestamps and error traces.

Grid strategy is optional and can be uncommented if implemented.

Resources
Binance Futures API Docs

Historical Data (Optional)

Fear & Greed Index (Bonus)

Author
Prajakta Ukirde
GitHub: https://github.com/prajaktaukirde
