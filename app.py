import os
import json
from dotenv import load_dotenv
from web3 import Web3
from decimal import Decimal
load_dotenv()

web3 = Web3(Web3.HTTPProvider(os.getenv('RPC_URL')))

if web3.is_connected():
    print("Connected to Ethereum node")


abi = json.loads(os.getenv('ABI'))
address = os.getenv('TOKEN_ADDRESS')

contract = web3.eth.contract(address =  address, abi = abi)

totalSupply = contract.functions.totalSupply().call()

# Get token decimals
decimals = contract.functions.decimals().call()

# Convert to readable token supply
total_supply = Decimal(totalSupply) / Decimal(10 ** decimals)

# Format with commas and 8 decimal places
print(f"Total Supply: {total_supply:,.8f} WBTC")
print("Token Name:", contract.functions.name().call())
print("Token Symbol:", contract.functions.symbol().call())
print("\n")

# Wallet address
wallet_address = "0xc3d688B66703497DAA19211EEdff47f25384cdc3"

balance = contract.functions.balanceOf(wallet_address).call()

print(f"balance: \n {Decimal(balance) / Decimal(10 ** decimals):,.8f} WBTC")