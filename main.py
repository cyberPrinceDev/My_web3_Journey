import os
from dotenv import load_dotenv

#load environment variables from .env file
load_dotenv()

from web3 import Web3

#initialize web3 instance with RPC URL from environment variable
web3 = Web3(Web3.HTTPProvider(os.getenv('RPC_URL')))

if web3.is_connected():
    print("Connected to Ethereum node")
