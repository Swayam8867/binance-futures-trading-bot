# Binance Futures Testnet Trading Bot

## Overview

A simplified Python-based CLI trading bot for Binance Futures Testnet (USDT-M).

This project allows users to place:
- MARKET orders
- LIMIT orders

with proper:
- input validation
- logging
- exception handling
- reusable project structure

---

## Features

- Place MARKET and LIMIT orders
- BUY and SELL support
- Binance Futures Testnet integration
- CLI-based input using argparse
- Structured project architecture
- Logging of requests, responses, and errors
- Exception handling for invalid input and API issues

---

## Project Structure

```bash
binance-futures-trading-bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── logging_config.py
│   ├── orders.py
│   └── validators.py
│
├── logs/
│   └── trading.log
│
├── .env.example
├── .gitignore
├── cli.py
├── README.md
└── requirements.txt
```

---

## Requirements

- Python 3.x
- Binance Futures Testnet account
- Binance Testnet API credentials

---

## Installation

### Clone Repository

```bash
git clone <your_repository_url>
cd binance-futures-trading-bot
```

---

### Create Virtual Environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory using `.env.example`

Example:

```env
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

---

## Binance Futures Testnet

Use Binance Futures Testnet credentials:

https://testnet.binancefuture.com

---

## Run Examples

### MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

### LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 95000
```

---

## Logging

Logs are automatically stored in:

```bash
logs/trading.log
```

Logs include:
- API request details
- API responses
- error messages

---

## Validation & Error Handling

The application handles:
- invalid order types
- invalid quantity values
- missing price for LIMIT orders
- API credential errors
- Binance API exceptions
- network-related failures

---

## Assumptions

- User already has Binance Futures Testnet account
- Testnet API credentials are active
- Internet connection is available

---

## Security Note

For security reasons:
- API credentials are NOT uploaded to GitHub
- `.env` is excluded using `.gitignore`

---

## Author

Swayam
