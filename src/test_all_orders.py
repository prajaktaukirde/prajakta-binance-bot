# test_all_orders.py
from logger import get_logger
from validation import validate_order
from market_orders import place_market_order
from limit_orders import place_limit_order
from advanced.oco import execute_oco
# from advanced.grid_strategy import run_grid  # Uncomment if implemented

logger = get_logger("bot_test")

def test_market_order():
    symbol = "BTCUSDT"
    side = "BUY"
    qty = 0.001

    logger.info("=== Testing Market Order ===")
    if validate_order(symbol, side, qty):
        result = place_market_order(symbol, side, qty, dry=True)
        logger.info("Market Order Result: %s", result)

def test_limit_order():
    symbol = "BTCUSDT"
    side = "SELL"
    qty = 0.001
    price = 45000

    logger.info("=== Testing Limit Order ===")
    if validate_order(symbol, side, qty, price=price):
        result = place_limit_order(symbol, side, qty, price, dry=True)
        logger.info("Limit Order Result: %s", result)

def test_oco_order():
    symbol = "BTCUSDT"
    side = "BUY"
    qty = 0.001
    stop_price = 44000
    stop_limit_price = 43990

    logger.info("=== Testing OCO Order ===")
    if validate_order(symbol, side, qty, stop_price=stop_price, tp_price=45000):
        # Corrected execute_oco call
        result = execute_oco(
            symbol,
            side,
            qty,
            stop_price,        # 44000
            stop_limit_price,  # 43990
            dry=True
        )
        logger.info("OCO Order Result: %s", result)




# Uncomment when your grid strategy is implemented
# def test_grid_order():
#     symbol = "BTCUSDT"
#     side = "BUY"
#     qty = 0.01
#     lower_price = 43000
#     upper_price = 45000
#     steps = 5
#
#     logger.info("=== Testing Grid Order ===")
#     if validate_order(symbol, side, qty):
#         result = run_grid(symbol, side, qty, lower_price, upper_price, steps, dry=True)
#         logger.info("Grid Order Result: %s", result)

if __name__ == "__main__":
    test_market_order()
    test_limit_order()
    test_oco_order()
    # test_grid_order()
