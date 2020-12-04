from datastructures.linked_list import DoublyLinkedList


class LruCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._location = {}
        self._dLinkList = DoublyLinkedList()

    def get(self, key):
        node = self._location.get(key)

        if node:
            self._dLinkList.move_to_head(node)
            return node.data

        return None

    def insert(self, key, value):
        if self._dLinkList.size == self._capacity:
            tail = self._dLinkList.tail
            self._dLinkList.remove_elem(tail)

            del self._location[tail.key]

        node = self._dLinkList.prepend(key, value)

        self._location[key] = node

        return True

    def delete(self, key):
        node = self._location.get(key)

        if node:
            del self._location[key]
            self._dLinkList.remove_elem(node)

        return True

    def flush(self):
        self._location = {}
