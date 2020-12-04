# Modified from https://dbader.org/blog/python-linked-list


class DListNode:
    """
    A node in a doubly-linked list.
    """

    def __init__(self, key=None, data=None, prev=None, next=None):
        self.key = key
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return repr(self.data)


class DoublyLinkedList:
    def __init__(self):
        """
        Create a new doubly linked list.
        Takes O(1) time.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return "[" + ", ".join(nodes) + "]"

    def prepend(self, key, data):
        """
        Insert a new element at the beginning of the list.
        Takes O(1) time.
        """
        new_head = DListNode(key=key, data=data, next=self.head)
        if self.head:
            self.head.prev = new_head
        self.head = new_head
        self.size += 1

        return new_head

    def append(self, key, data):
        """
        Insert a new element at the end of the list.
        Modified: Takes O(1) time.
        """
        if not self.head:
            self.head = DListNode(key=key, data=data)
            self.tail = self.head
            self.size += 1
            return self.head

        curr = self.tail
        curr.next = DListNode(key=key, data=data, prev=curr)
        self.tail = curr.next
        self.size += 1
        return curr.next

    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr  # Will be None if not found

    def remove_elem(self, node):
        """
        Unlink an element from the list.
        Takes O(1) time.
        """
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node is self.head:
            self.head = node.next
        node.prev = None
        node.next = None
        self.size -= 1

    def reverse(self):
        """
        Reverse the list in-place.
        Takes O(n) time.
        """
        curr = self.head
        prev_node = None
        while curr:
            prev_node = curr.prev
            curr.prev = curr.next
            curr.next = prev_node
            curr = curr.prev
        self.head = prev_node.prev
