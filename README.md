# Binance Futures Testnet Trading Bot

## Objective

This project is a Python-based trading bot that interacts with Binance Futures Testnet (USDT-M). It supports placing MARKET and LIMIT orders for both BUY and SELL sides through a Command Line Interface (CLI) and a lightweight Streamlit UI.

---

## Features

* Place MARKET Orders
* Place LIMIT Orders
* BUY and SELL support
* Binance Futures Testnet Integration
* Input Validation
* Error Handling
* Logging
* CLI Interface
* Lightweight Streamlit UI
* Modular Project Structure

---

## Project Structure

trading_bot/

├── bot/

│   ├── **init**.py

│   ├── client.py

│   ├── orders.py

│   ├── validators.py

│   └── logging_config.py

│

├── logs/

│   ├── trading_bot.log

│   ├── market_order.log

│   └── limit_order.log

│

├── ui.py

├── cli.py

├── .env

├── requirements.txt

└── README.md

---

## Assumptions

1. User has a Binance Futures Testnet account.
2. User has generated Testnet API credentials.
3. Testnet USDT balance is available.
4. Internet connection is available.
5. Orders are placed only on Binance Futures Testnet.

---

## Setup Steps

### 1. Clone Repository

git clone <repository_url>

cd trading_bot

### 2. Create Virtual Environment

python -m venv venv

### 3. Activate Environment

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate

### 4. Install Dependencies

pip install -r requirements.txt

### 5. Configure Environment Variables

Create .env file:

BINANCE_API_KEY=YOUR_API_KEY

BINANCE_SECRET_KEY=YOUR_SECRET_KEY

---

## Running the Application

### MARKET BUY

python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001

### MARKET SELL

python cli.py --symbol BTCUSDT --side SELL --order-type MARKET --quantity 0.001

### LIMIT BUY

python cli.py --symbol BTCUSDT --side BUY --order-type LIMIT --quantity 0.001

### LIMIT SELL

python cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.001

### LIMIT BUY WITH CUSTOM PRICE

python cli.py --symbol BTCUSDT --side BUY --order-type LIMIT --quantity 0.001 --price 63000

---

## Running Lightweight UI

streamlit run ui.py

Open browser:

http://localhost:8501

---

## Logging

Application logs are stored in:

logs/trading_bot.log

Sample order logs:

logs/market_order.log

logs/limit_order.log

---

## Technologies Used

* Python 3.x
* python-binance
* Click
* Streamlit
* python-dotenv
