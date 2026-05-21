import os
from pathlib import Path

from dotenv import load_dotenv
from binance.client import Client

# Get root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env from root folder
env_path = BASE_DIR / ".env"

print("ENV PATH:", env_path)

load_dotenv(dotenv_path=env_path)

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

print("API KEY FOUND:", bool(api_key))
print("SECRET FOUND:", bool(api_secret))

if not api_key or not api_secret:
    raise ValueError(
        "Missing Binance API credentials. "
        "Please check your .env file."
    )

client = Client(api_key, api_secret)

# Binance Futures Testnet URL
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

print("CLIENT CONNECTED SUCCESSFULLY")