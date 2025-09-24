"""
Conceptual OCO (One Cancels the Other) example.
This file shows how to structure an OCO: a take-profit limit and a stop-limit.
It's a high-level example and uses dry-run mode.
"""

from logger import get_logger

logger = get_logger("oco")

def prepare_oco(symbol, side, qty, tp_price, stop_price, stop_limit_price, dry=True):
    """
    Prepares a conceptual OCO order.
    tp_price: Take Profit price
    stop_price: Stop trigger price
    stop_limit_price: Stop-limit order price
    """
    logger.info("Preparing OCO for %s", symbol)
    tp = {"type": "LIMIT", "side": "SELL" if side == "BUY" else "BUY", "price": tp_price, "quantity": qty}
    stop = {"type": "STOP_LIMIT", "side": "SELL" if side == "BUY" else "BUY",
            "stopPrice": stop_price, "price": stop_limit_price, "quantity": qty}
    oco = {"take_profit": tp, "stop_limit": stop}
    
    if dry:
        logger.info("[DRY RUN] OCO prepared: %s", oco)
        return {"status": "dry", "oco": oco}

    logger.error("Live OCO placement not implemented in example.")
    return {"status": "failed", "reason": "live-not-implemented"}


def execute_oco(symbol, side, qty, stop_price, stop_limit_price, dry=True):
    tp_price = 45000  # take-profit
    logger.info("Preparing OCO for %s", symbol)
    tp = {"type":"LIMIT","side": "SELL" if side=="BUY" else "BUY","price":tp_price,"quantity":qty}
    stop = {"type":"STOP_LIMIT","side": "SELL" if side=="BUY" else "BUY","stopPrice":stop_price,"price":stop_limit_price,"quantity":qty}
    oco = {"take_profit":tp, "stop_limit":stop}
    if dry:
        logger.info("[DRY RUN] OCO prepared: %s", oco)
        return {"status":"dry","oco":oco}
    logger.error("Live OCO placement not implemented.")
    return {"status":"failed","reason":"live-not-implemented"}
