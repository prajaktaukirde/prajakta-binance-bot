# Prajakta Binance Bot

## Overview
A Python-based Binance Futures trading bot that supports **Market**, **Limit**, and **OCO (One Cancels Other)** orders.  
Includes basic order validation, logging, and optional advanced strategies like **TWAP** and **Grid**.

---

## Features
- **Market Orders**: Instant buy/sell at market price.  
- **Limit Orders**: Buy/sell at a specific price.  
- **OCO Orders**: Combines take-profit and stop-limit in a single order.  
- **Logging**: All actions, errors, and dry-run outputs saved in `src/bot.log`.  
- **Advanced Orders**: TWAP and Grid strategies available in `src/advanced/`.  

---

## Folder Structure
prajakta-binance-bot/
├── src/
│ ├── market_orders.py → Market order logic
│ ├── limit_orders.py → Limit order logic
│ ├── validation.py → Order validation
│ ├── logger.py → Logging setup
│ ├── test_all_orders.py → Test all order types
│ └── advanced/
│ ├── oco.py → OCO order logic
│ ├── twap.py → TWAP strategy
│ └── grid_strategy.py → Grid strategy (optional)
├── bot.log → Logs for dry-run & API executions
├── README.md → Project documentation
└── report.pdf → Screenshots & explanations


---

## Quick Start

### Order Types & Commands

| Order Type            | Command / Script Example                        | Notes                                      |
|-----------------------|------------------------------------------------|-------------------------------------------|
| Market Order          | `python src/market_orders.py BTCUSDT BUY 0.01` | Executes a market buy order               |
| Limit Order           | `python src/limit_orders.py BTCUSDT SELL 0.01 45000` | Places a limit sell at 45,000 USDT       |
| Test All Orders       | `python src/test_all_orders.py`               | Runs dry-run for Market, Limit, OCO      |
| OCO Order (Advanced)  | `python src/advanced/oco.py`                  | Execute OCO take-profit + stop-limit     |
| TWAP Strategy         | `python src/advanced/twap.py`                 | Time-weighted average price strategy     |
| Grid Strategy         | `python src/advanced/grid_strategy.py`        | Optional grid trading strategy           |

---

## Setup

### Clone Repository
```bash
git clone https://github.com/prajaktaukirde/prajakta-binance-bot.git
cd prajaktaukirde-binance-bot
Create Virtual Environment
bash
Copy code
python -m venv venv
# Windows PowerShell
.\venv\Scripts\Activate.ps1
# Windows CMD
venv\Scripts\activate.bat
# macOS/Linux
source venv/bin/activate
Install Dependencies
bash
Copy code
pip install -r requirements.txt
Configure API Keys
Set your Binance API keys in config.py or as environment variables:

python
Copy code
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
Usage
Market Order
bash
Copy code
python src/market_orders.py BTCUSDT BUY 0.01
Limit Order
bash
Copy code
python src/limit_orders.py BTCUSDT SELL 0.01 45000
Test All Orders (Dry-run)
bash
Copy code
python src/test_all_orders.py
Advanced Orders
OCO Orders: python src/advanced/oco.py

TWAP Strategy: python src/advanced/twap.py

Grid Strategy (optional): python src/advanced/grid_strategy.py

Logging
Log File
All actions, errors, and dry-run outputs are logged in src/bot.log.

Example Log Entries
less
Copy code
[INFO] Preparing MARKET order | BTCUSDT BUY 0.01
[INFO] [DRY RUN] Order prepared: {...}
[ERROR] Invalid order: ...
Notes
Ensure your virtual environment is active before running commands.

Advanced strategies (TWAP/Grid) are optional but included for bonus evaluation.

All logs help track executions and debug issues.
