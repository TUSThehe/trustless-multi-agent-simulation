# blockchain.py
import hashlib

class Blockchain:
    def __init__(self):
        self.chain = []

    def add_record(self, agent_id, action):
        block = {
            'agent_id': agent_id,
            'action': action,
            'hash': self.hash_action(agent_id, action)
        }
        self.chain.append(block)
        print(f"[Blockchain] Action recorded: {block}")
        
    def hash_action(self, agent_id, action):
        return hashlib.sha256(f"{agent_id}:{action}".encode()).hexdigest()

    def display_chain(self):
        print("\n[Blockchain Ledger]")
        for block in self.chain:
            print(block)
        print("")
