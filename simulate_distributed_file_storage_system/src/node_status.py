from src.node import Node

class NodeStatus:
    def __init__(self):
        # Dictionary to track online/offline status by Node ID
        self._status = {}

    def go_offline(self, node: Node) -> None:
        self._status[node.id] = False

    def come_online(self, node: Node) -> None:
        self._status[node.id] = True

    def is_online(self, node: Node) -> bool:
        return self._status.get(node.id, False)
