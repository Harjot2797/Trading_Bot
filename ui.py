import streamlit as st

from bot.client import BinanceFuturesClient
from bot.orders import OrderManager
from bot.logging_config import get_logger

st.set_page_config(
    page_title="Binance Futures Testnet Bot",
    layout="centered"
)

st.title("🚀 Binance Futures Testnet Trading Bot")

symbol = st.text_input(
    "Symbol",
    value="BTCUSDT"
)

side = st.selectbox(
    "Side",
    ["BUY", "SELL"]
)

order_type = st.selectbox(
    "Order Type",
    ["MARKET", "LIMIT"]
)

quantity = st.number_input(
    "Quantity",
    min_value=0.001,
    value=0.001
)

price = None

if order_type == "LIMIT":
    price = st.number_input(
        "Price",
        min_value=1.0,
        value=63000.0
    )

if st.button("Place Order"):

    try:
        logger = get_logger()

        binance_client = BinanceFuturesClient()
        client = binance_client.get_client()

        manager = OrderManager(
            client,
            logger
        )

        if order_type == "MARKET":
            response = manager.place_market_order(
                symbol,
                side,
                quantity
            )
        else:
            response = manager.place_limit_order(
                symbol,
                side,
                quantity,
                price
            )

        st.success("Order placed successfully")

        st.json({
            "orderId": response.get("orderId"),
            "status": response.get("status"),
            "executedQty": response.get("executedQty"),
            "avgPrice": response.get("avgPrice")
        })

    except Exception as e:
        st.error(str(e))