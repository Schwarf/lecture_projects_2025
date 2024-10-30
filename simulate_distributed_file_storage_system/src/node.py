from typing import Optional

from src.store_manager import StorageManager


class Node:
    def __init__(self, node_id: str, storage_dir: str):
        self.id = node_id
        self.storage_dir = storage_dir
        self.storage_manager = StorageManager(storage_dir)


    def replicate_chunk(self, chunk_id: str, target_node: 'Node') -> None:
        chunk_data = self.storage_manager.retrieve_chunk(chunk_id)
        if chunk_data:
            target_node.storage_manager.store_chunk(chunk_id, chunk_data)
            print(f"Replicated chunk {chunk_id} to node {target_node.id}")
