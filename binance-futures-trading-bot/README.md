# Binance Futures Testnet Trading Bot

## Overview

A simple Python CLI trading bot for Binance Futures Testnet (USDT-M).

Features:
- MARKET orders
- LIMIT orders
- BUY and SELL support
- Input validation
- Logging
- Exception handling

---

## Setup

### Clone Repository

```bash
git clone <your_repo_url>
cd binance-futures-trading-bot
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file using `.env.example`

Example:

```env
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

---

## Run Examples

### MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 95000
```

---

## Assumptions

- Binance Futures Testnet account is already created
- Testnet API credentials are valid
- Internet connection is available

---

## Logs

Logs are stored in:

```txt
logs/trading.log
```