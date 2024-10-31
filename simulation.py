# simulation.py
import random
from time import sleep
from distributed_key_manager import DistributedKeyManager
from blockchain import Blockchain
from dao import DAO
from agent import Agent

def run_simulation():
    key_manager = DistributedKeyManager()
    blockchain = Blockchain()
    dao = DAO()
    
    agents = [Agent(i, key_manager, blockchain, dao) for i in range(1, 4)]

    print("\n=== Trustless Multi-Agent Simulation ===\n")

    # Each agent performs an action
    for agent in agents:
        action = random.choice(["post_message", "analyze_data", "trade"])
        agent.perform_action(action)
        sleep(1)  # Simulate time between actions

    # Agent 1 proposes an upgrade
    proposal_text = "Upgrade agent memory"
    proposal_id = agents[0].propose_upgrade(proposal_text)
    sleep(1)

    # Agents vote on the proposal
    for agent in agents:
        agent.vote_on_proposal(proposal_id)
        sleep(1)

    # DAO enacts proposals based on votes
    dao.enact_proposals()

    # Display the blockchain ledger
    blockchain.display_chain()
    # Display DAO proposals
    dao.list_proposals()
