from src.node import Node


class LeadershipRole:
    def __init__(self):
        # Dictionary to store leadership status by Node ID
        self._leader_status = {}

    def make_leader(self, node: Node) -> None:
        self._leader_status[node.id] = True

    def remove_leadership(self, node: Node) -> None:
        self._leader_status[node.id] = False

    def is_leader(self, node: Node) -> bool:
        return self._leader_status.get(node.id, False)


