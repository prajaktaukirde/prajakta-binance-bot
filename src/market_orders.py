"""Market order example for Binance USDT-M Futures (dry-run by default).
Usage:
    python src/market_orders.py BTCUSDT BUY 0.001 --dry
Notes:
 - This script validates inputs, logs actions, and demonstrates how to prepare an order.
 - It WILL NOT place real orders unless API keys are provided and --dry is omitted.
"""
import argparse
import os
from logger import get_logger
logger = get_logger("market_orders")

def validate_symbol(s):
    if not s.endswith("USDT"):
        raise ValueError("Symbol must end with USDT for USDT-M Futures.")
    return s.upper()

def validate_side(side):
    s = side.upper()
    if s not in ("BUY","SELL"):
        raise ValueError("Side must be BUY or SELL.")
    return s

def validate_qty(q):
    q = float(q)
    if q <= 0:
        raise ValueError("Quantity must be positive.")
    return q

def place_market_order(symbol, side, quantity, dry=True):
    logger.info("Preparing MARKET order | %s %s %s", symbol, side, quantity)
    order = {
        "symbol": symbol,
        "side": side,
        "type": "MARKET",
        "quantity": quantity
    }
    if dry:
        logger.info("[DRY RUN] Order prepared: %s", order)
        return {"status":"dry","order":order}
    # Real trading code would go here (python-binance or requests to Binance API).
    # We intentionally do not implement live key usage in this example.
    logger.error("Live order placement not implemented in example.")
    return {"status":"failed","reason":"live-not-implemented"}

def main():
    p = argparse.ArgumentParser()
    p.add_argument("symbol")
    p.add_argument("side")
    p.add_argument("quantity")
    p.add_argument("--dry", action="store_true", help="Do not actually place order")
    args = p.parse_args()
    try:
        sym = validate_symbol(args.symbol)
        side = validate_side(args.side)
        qty = validate_qty(args.quantity)
    except Exception as e:
        logger.exception("Validation error: %s", e)
        return
    res = place_market_order(sym, side, qty, dry=args.dry)
    logger.info("Result: %s", res)

if __name__ == "__main__":
    main()
