# Prajakta Binance Bot

## Overview
A Python-based Binance Futures trading bot that supports **Market**, **Limit**, and **OCO (One Cancels Other)** orders.  
Includes basic order validation, logging, and optional advanced strategies like **TWAP** and **Grid**.

---

## Features
- **Market Orders**: Instant buy/sell at market price.  
- **Limit Orders**: Buy/sell at a specific price.  
- **OCO Orders**: Combines take-profit and stop-limit in a single order.  
- **Logging**: All actions, errors, and dry-run outputs saved in `bot.log`.  
- **Advanced Orders**: TWAP and Grid strategies available in `src/advanced/`.

---

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

yaml
Copy code

---

## Setup

### 1. Clone Repository
```bash
git clone https://github.com/prajaktaukirde/prajakta-binance-bot.git
cd prajakta-binance-bot
2. Create Virtual Environment
bash
Copy code
python -m venv venv
# Windows PowerShell
.\venv\Scripts\Activate.ps1
# Windows CMD
venv\Scripts\activate.bat
# macOS/Linux
source venv/bin/activate
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Configure API Keys
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
Use scripts in src/advanced/ for TWAP or Grid strategies.

Logging
All actions, errors, and dry-run outputs are logged in bot.log.

Example log:

less
Copy code
[INFO] Preparing MARKET order | BTCUSDT BUY 0.01
[INFO] [DRY RUN] Order prepared: {...}
[ERROR] Invalid order: ...
Submission
Submit .zip file: prajakta_binance_bot.zip with folder structure intact.

Push code to private GitHub repo: https://github.com/prajaktaukirde/prajakta-binance-bot

Include README.md and report.pdf.

References
Binance Futures API Docs: https://binance-docs.github.io/apidocs/futures/en/

Historical Data: Download

Fear & Greed Index (Bonus): Download
