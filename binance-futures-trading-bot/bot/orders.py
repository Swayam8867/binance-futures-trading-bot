from bot.client import client
from bot.logging_config import logger


def place_order(symbol, side, order_type, quantity, price=None):
    try:
        logger.info(
            f"REQUEST -> Symbol={symbol}, Side={side}, "
            f"Type={order_type}, Quantity={quantity}, Price={price}"
        )

        params = {
            "symbol": symbol.upper(),
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        response = client.futures_create_order(**params)

        logger.info(f"RESPONSE -> {response}")

        return response

    except Exception as e:
        logger.error(f"ERROR -> {str(e)}")
        raise