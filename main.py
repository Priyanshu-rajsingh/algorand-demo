# main.py
from algosdk.v2client import indexer

# Replace with your Indexer URL and token if you have one
indexer_client = indexer.IndexerClient("", "https://testnet-algorand.api.purestake.io/idx2")

status = indexer_client.health()
print("Indexer status:", status)
