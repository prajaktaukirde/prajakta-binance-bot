"""Limit order example (dry-run).
Usage:
    python src/limit_orders.py BTCUSDT BUY 0.001 45000 --dry
"""
import argparse
from logger import get_logger
logger = get_logger("limit_orders")

def validate_price(p):
    p = float(p)
    if p <= 0:
        raise ValueError("Price must be positive.")
    return p

def place_limit_order(symbol, side, quantity, price, dry=True):
    logger.info("Preparing LIMIT order | %s %s %s @ %s", symbol, side, quantity, price)
    order = {
        "symbol": symbol,
        "side": side,
        "type": "LIMIT",
        "quantity": quantity,
        "price": price,
    }
    if dry:
        logger.info("[DRY RUN] Limit order prepared: %s", order)
        return {"status":"dry","order":order}
    logger.error("Live limit order placement not implemented in example.")
    return {"status":"failed","reason":"live-not-implemented"}

def main():
    import sys
    if len(sys.argv) < 5:
        print("Usage: python src/limit_orders.py SYMBOL SIDE QTY PRICE [--dry]")
        return
    sym, side, qty, price = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4])
    dry = "--dry" in sys.argv
    try:
        from market_orders import validate_symbol, validate_side, validate_qty
        sym = validate_symbol(sym)
        side = validate_side(side)
        qty = validate_qty(qty)
        price = validate_price(price)
    except Exception as e:
        logger.exception("Validation error: %s", e)
        return
    res = place_limit_order(sym, side, qty, price, dry=dry)
    logger.info("Result: %s", res)

if __name__ == "__main__":
    main()
