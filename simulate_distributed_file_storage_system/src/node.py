from typing import Optional

from src.store_manager import StorageManager


class Node:
    def __init__(self, node_id: str, storage_dir: str):
        self.id = node_id
        self.storage_dir = storage_dir
        self.storage_manager = StorageManager(storage_dir)


