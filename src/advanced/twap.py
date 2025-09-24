"""Simple TWAP strategy example.
Splits a total quantity into N equal chunks executed at regular intervals (dry-run).
"""
import time
from logger import get_logger
logger = get_logger("twap")

def execute_twap(symbol, side, total_qty, intervals=5, interval_seconds=10, dry=True):
    chunk = float(total_qty) / intervals
    logger.info("TWAP: %s %s total=%s into %s chunks", symbol, side, total_qty, intervals)
    orders = []
    for i in range(intervals):
        order = {"symbol":symbol,"side":side,"type":"MARKET","quantity":round(chunk,8),"chunk_index":i+1}
        if dry:
            logger.info("[DRY RUN] TWAP chunk prepared: %s", order)
            orders.append(order)
        else:
            logger.error("Live TWAP execution not implemented in example.")
    return {"status":"dry","orders":orders}
