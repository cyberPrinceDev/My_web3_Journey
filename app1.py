"""
Sending transactions on Ethereum using Web3.py.

This script demonstrates how to:
- Build a transaction
- Sign a transaction
- Broadcast a transaction
- Confirm a transaction
"""

import os 
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

web3 = Web3(Web3.HTTPProvider(os.getenv('ganache_url')))

if web3.is_connected():
    print("Connected to Ethereum node")


account_1 = "0x14DeBc3cc91DDA24F2f781f28C3D8790b49c9936"
account_2 = "0x750715608b29BB127CF0aC4c5Ed47829c1F7dC1C"

private_key = "0x9e7d3555db0eaedbbceefc35661c84c2fbaf15be67ecaf5559f50690ea51d3bd"

# Get nonce
nonce = web3.eth.get_transaction_count(account_1)

# Build transaction
tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.to_wei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.eth.gas_price,
    'chainId': web3.eth.chain_id
}

# Sign transaction
signed_tx = web3.eth.account.sign_transaction(tx, private_key)

# Broadcast transaction
tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)

print("Transaction Hash:", web3.to_hex(tx_hash))

# Wait for transaction confirmation
receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

print("Transaction Status:", receipt.status)