# distributed_key_manager.py
import secrets

class DistributedKeyManager:
    def __init__(self):
        self.keys = {}

    def generate_key(self, agent_id):
        key = secrets.token_hex(16)
        self.keys[agent_id] = key
        print(f"[Key Manager] Generated key for Agent {agent_id}: {key}")
        return key

    def get_key(self, agent_id):
        return self.keys.get(agent_id, None)
