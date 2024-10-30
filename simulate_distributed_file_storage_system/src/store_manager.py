from typing import Optional

from src.node import Node


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
