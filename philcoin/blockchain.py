import json
import random
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
        self.chain.append(self.new_block())

    def new_block(self):
        # Generates a new block and adds it to the chain
        block = {
            "index": len(self.chain),
            "timestamp": datetime.utcnow().isoformat(),
            "transactions": self.pending_transactions,
            "previous_hash": self.last_block["hash"] if self.last_block else None,
            "nonce": format(random.getrandbits(64), "x")
        }
        # Get the hash of this new block and add it to the block
        block_hash = self.hash(block)
        block["hash"] = block_hash
        # Reset the list of pending transactions
        self.pending_transactions = []
        return block

    @staticmethod
    def hash(block):
        # hashes a block. Ensure the dictionary is sorted or we will end up with inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

    @property
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

    def proof_of_work(self):
        while True:
            new_block = self.new_block()
            if self.valid_block(new_block):
                break
        self.chain.append(new_block)
        print("Found a new block: ", new_block)

    @staticmethod
    def valid_block(block):
        return block["hash"].startswith("00000")
