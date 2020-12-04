from .lib.linked_list import DoublyLinkedList


class LruCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._location = {}
        self._dLinkList = DoublyLinkedList()

    def get(self, key):
        node = self._location.get(key)

        if node:
            return node.data

        return None

    def insert(self, key, value):
        if self._dLinkList.size == self._capacity:
            head = self._dLinkList.head
            self._dLinkList.remove_elem(head)

            del self._location[head.key]

        node = self._dLinkList.append(key, value)

        self._location[key] = node

        return True

    def delete(self, key):
        node = self._location.get(key)

        if node:
            del self._location[key]
            self._dLinkList.remove_elem(node)

        return True
