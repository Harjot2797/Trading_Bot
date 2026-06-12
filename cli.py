import click

from bot.client import BinanceFuturesClient
from bot.orders import OrderManager
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from bot.logging_config import get_logger


@click.command()
@click.option(
    "--symbol",
    required=True,
    help="Example BTCUSDT"
)
@click.option(
    "--side",
    required=True,
    help="BUY or SELL"
)
@click.option(
    "--order-type",
    required=True,
    help="MARKET or LIMIT"
)
@click.option(
    "--quantity",
    required=True
)
@click.option(
    "--price",
    required=False,
    type=float
)
def run(
    symbol,
    side,
    order_type,
    quantity,
    price
):

    logger = get_logger()

    try:

        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_quantity(quantity)

        if price:
            price = validate_price(price)

        # Create Binance Client
        binance_client = BinanceFuturesClient()

        current_price = binance_client.get_current_price(
            symbol
        )

        print(
            f"\nCurrent Market Price: {current_price}"
        )

        client = binance_client.get_client()

        manager = OrderManager(
            client,
            logger
        )

        print("\n========================")
        print("ORDER REQUEST")
        print("========================")

        print(f"Symbol   : {symbol}")
        print(f"Side     : {side}")
        print(f"Type     : {order_type}")
        print(f"Quantity : {quantity}")

        if order_type == "MARKET":

            response = manager.place_market_order(
                symbol,
                side,
                quantity
            )

        else:

            # Auto generate valid LIMIT price
            if not price:

                if side == "BUY":
                    price = round(
                        current_price * 0.99,
                        2
                    )
                else:
                    price = round(
                        current_price * 1.01,
                        2
                    )

                print(
                    f"Auto-selected LIMIT Price: {price}"
                )

            # Validate price range
            lower_limit = current_price * 0.95
            upper_limit = current_price * 1.05

            if not (
                lower_limit <= price <= upper_limit
            ):

                raise ValueError(
                    f"LIMIT price must be between "
                    f"{round(lower_limit, 2)} "
                    f"and "
                    f"{round(upper_limit, 2)}"
                )

            print(f"Price    : {price}")

            response = manager.place_limit_order(
                symbol,
                side,
                quantity,
                price
            )

        print("\n========================")
        print("ORDER RESPONSE")
        print("========================")

        print(
            f"Order ID      : "
            f"{response.get('orderId')}"
        )

        print(
            f"Status        : "
            f"{response.get('status')}"
        )

        print(
            f"Executed Qty  : "
            f"{response.get('executedQty')}"
        )

        print(
            f"Avg Price     : "
            f"{response.get('avgPrice')}"
        )

        print("\nSUCCESS")

    except Exception as e:

        logger.error(str(e))

        print("\nFAILED")
        print(str(e))


if __name__ == "__main__":
    run()