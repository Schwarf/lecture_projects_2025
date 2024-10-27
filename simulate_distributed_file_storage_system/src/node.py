from typing import Optional

class Node:
    def __init__(self, node_id: str, storage_dir: str):
        self.id = node_id
        self.storage_dir = storage_dir
        self.storage_manager = StorageManager(storage_dir)


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


class StorageManager:
    def __init__(self, storage_dir: str):
        self.storage_dir = storage_dir
        self._storage = {}  # Dictionary to simulate storage of chunks

    def store_chunk(self, chunk_id: str, chunk_data: bytes) -> None:
        self._storage[chunk_id] = chunk_data
        print(f"Stored chunk {chunk_id} in {self.storage_dir}")

    def retrieve_chunk(self, chunk_id: str) -> Optional[bytes]:
        return self._storage.get(chunk_id)

    def delete_chunk(self, chunk_id: str) -> None:
        if chunk_id in self._storage:
            del self._storage[chunk_id]
            print(f"Deleted chunk {chunk_id} from {self.storage_dir}")

    def replicate_chunk(self, chunk_id: str, target_node: Node) -> None:
        chunk_data = self.retrieve_chunk(chunk_id)
        if chunk_data:
            target_node.storage_manager.store_chunk(chunk_id, chunk_data)
            print(f"Replicated chunk {chunk_id} to node {target_node.id}")
