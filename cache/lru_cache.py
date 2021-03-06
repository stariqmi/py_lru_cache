import pickle
import time

from .datastructures.linked_list import DoublyLinkedList


class LruCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._hash_map = {}
        self._doubly_linked_list = DoublyLinkedList()

    def get(self, key):
        node = self._hash_map.get(key)

        if node:
            self._doubly_linked_list.move_to_front(node)
            return node.data

        return None

    def update(self, key, value):
        node = self._hash_map.get(key)

        node.data = value
        self._doubly_linked_list.move_to_front(node)

    def insert(self, key, value):
        # If key already exists, just move to front
        if key in self._hash_map:
            return self.update(key, value)

        node = self._doubly_linked_list.prepend(key, value)
        self._hash_map[key] = node

        # If exceeds capacity, remove least recently used
        if self._doubly_linked_list.size > self._capacity:
            tail = self._doubly_linked_list.tail
            self._doubly_linked_list.remove_elem(tail)

            del self._hash_map[tail.key]

    def delete(self, key):
        node = self._hash_map.get(key)

        if node:
            del self._hash_map[key]
            self._doubly_linked_list.remove_elem(node)

    def flush(self):
        self._hash_map = {}
        self._doubly_linked_list = DoublyLinkedList()

    def backup(self, file=None):
        file_path = file if file else f"/tmp/backup.{int(time.time())}.p"
        with open(file_path, "wb") as f:
            pickle.dump(
                {
                    "capacity": self._capacity,
                    "hash_map": self._hash_map,
                    "doubly_linked_list": self._doubly_linked_list,
                },
                f,
            )

    def restore(self, file):
        with open(file, "rb") as f:
            data = pickle.load(f)
            self._capacity = data["capacity"]
            self._hash_map = data["hash_map"]
            self._doubly_linked_list = data["doubly_linked_list"]
