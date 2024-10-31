# agent.py
from distributed_key_manager import DistributedKeyManager
from blockchain import Blockchain
from dao import DAO

class Agent:
    def __init__(self, agent_id, key_manager, blockchain, dao):
        self.agent_id = agent_id
        self.key = key_manager.generate_key(agent_id)
        self.blockchain = blockchain
        self.dao = dao

    def perform_action(self, action):
        print(f"[Agent {self.agent_id}] Performing action: {action}")
        self.blockchain.add_record(self.agent_id, action)

    def propose_upgrade(self, proposal):
        proposal_id = self.dao.propose_upgrade(proposal)
        return proposal_id

    def vote_on_proposal(self, proposal_id):
        self.dao.vote(proposal_id)
