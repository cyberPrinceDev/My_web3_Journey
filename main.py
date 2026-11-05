import os
from dotenv import load_dotenv

#load environment variables from .env file
load_dotenv()

from web3 import Web3

#initialize web3 instance with RPC URL from environment variable
web3 = Web3(Web3.HTTPProvider(os.getenv('RPC_URL')))

if web3.is_connected():
    print("Connected to Ethereum node")

print(f"Current block number: {web3.eth.block_number}")

wallet = "0xc953CDd38A1C3DA7676f75B602208DC502D094bB"

balance = web3.eth.get_balance(wallet)

print(f"Balance of wallet {wallet}: \n {web3.from_wei(balance, 'ether')} ETH")