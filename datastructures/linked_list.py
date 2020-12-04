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

    def move_to_head(self, node):
        if node is not self.head:
            self.remove_elem(node)
            self.prepend(node.key, node.data)

    def prepend(self, key, data):
        """
        Insert a new element at the beginning of the list.
        Takes O(1) time.
        """
        new_head = DListNode(key=key, data=data, next=self.head)
        if self.head:
            self.head.prev = new_head
        else:
            self.tail = new_head

        self.head = new_head
        self.size += 1

        return new_head

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
        if node is self.tail:
            self.tail = node.prev

        node.prev = None
        node.next = None
        self.size -= 1
