from datastructures.linked_list import DoublyLinkedList


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

    def insert(self, key, value):
        if self._doubly_linked_list.size == self._capacity:
            tail = self._doubly_linked_list.tail
            self._doubly_linked_list.remove_elem(tail)

            del self._hash_map[tail.key]

        node = self._doubly_linked_list.prepend(key, value)

        self._hash_map[key] = node

    def delete(self, key):
        node = self._hash_map.get(key)

        if node:
            del self._hash_map[key]
            self._doubly_linked_list.remove_elem(node)

    def flush(self):
        self._hash_map = {}
        self._doubly_linked_list = DoublyLinkedList()
