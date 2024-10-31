# dao.py
class DAO:
    def __init__(self):
        self.proposals = []
        self.votes = {}

    def propose_upgrade(self, proposal):
        proposal_id = len(self.proposals) + 1
        self.proposals.append({'id': proposal_id, 'proposal': proposal, 'votes': 0})
        print(f"[DAO] New proposal added: {proposal}")
        return proposal_id

    def vote(self, proposal_id):
        if proposal_id <= len(self.proposals):
            self.proposals[proposal_id - 1]['votes'] += 1
            print(f"[DAO] Vote cast for proposal {proposal_id}")
        else:
            print("[DAO] Invalid proposal ID")

    def list_proposals(self):
        print("\n[DAO Proposals]")
        for proposal in self.proposals:
            print(proposal)
        print("")

    def enact_proposals(self):
        for proposal in self.proposals:
            if proposal['votes'] > 1:  # Threshold for enacting
                print(f"[DAO] Enacting proposal: {proposal['proposal']} with {proposal['votes']} votes")
            else:
                print(f"[DAO] Proposal {proposal['proposal']} did not pass\n")
