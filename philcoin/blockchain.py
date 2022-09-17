import json

from datetime import datetime
from hashlib import sha256


class Blockchain(object):
    """A simple Blockchain class"""

    def __init__(self):
        print("Initiating......")
        self.chain = []
        self.pending_transactions = []

        # create the genesis block
        print("Creating the genesis block")
        self.new_block()

    def new_block(self, previous_hash=None):
        # Generates a new block and adds it to the chain
        block = {
            "index": len(self.chain),
            "timestamp": datetime.utcnow().isoformat(),
            "transactions": self.pending_transactions,
            "previous_hash": previous_hash
        }
        # Get the hash of this new block and add it to the block
        block_hash = self.hash(block)
        block["hash"] = block_hash
        # Reset the list of pending transactions
        self.pending_transactions = []
        # add the block to the chain
        self.chain.append(block)
        print(f"Created block {block['index']}")
        return block

    @staticmethod
    def hash(block):
        # hashes a block. Ensure the dictionary is sorted or we will end up with inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

    def last_block(self):
        # Gets the latest block in the chain (if there are blocks)
        return self.chain[-1] if self.chain else None

    def new_transaction(self, sender, recipient, amount):
        # Adds a new transaction to the list of pending transactions
        self.pending_transactions.append({
            "recipient": recipient,
            "sender": sender,
            "amount": amount
        })
