# src/validation.py

def validate_order(symbol, side, quantity, price=None, stop_price=None, tp_price=None):
    # Check symbol
    if not isinstance(symbol, str) or len(symbol) < 5:
        raise ValueError(f"Invalid symbol: {symbol}")
    
    # Check side
    if side not in ["BUY", "SELL"]:
        raise ValueError(f"Invalid side: {side}. Must be BUY or SELL")
    
    # Check quantity
    if not (isinstance(quantity, float) or isinstance(quantity, int)) or quantity <= 0:
        raise ValueError(f"Invalid quantity: {quantity}")
    
    # Check prices
    if price is not None and price <= 0:
        raise ValueError(f"Invalid price: {price}")
    if stop_price is not None and stop_price <= 0:
        raise ValueError(f"Invalid stop price: {stop_price}")
    if tp_price is not None and tp_price <= 0:
        raise ValueError(f"Invalid take-profit price: {tp_price}")
    
    # Check logical OCO thresholds
    if stop_price and tp_price:
        if side == "BUY" and stop_price > tp_price:
            raise ValueError(f"Stop price {stop_price} should be less than take-profit {tp_price} for BUY")
        if side == "SELL" and stop_price < tp_price:
            raise ValueError(f"Stop price {stop_price} should be greater than take-profit {tp_price} for SELL")
    
    return True
