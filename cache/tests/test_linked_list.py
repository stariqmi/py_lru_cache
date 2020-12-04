import pytest

from cache.datastructures.linked_list import DoublyLinkedList


@pytest.fixture
def linked_list():
    ll = DoublyLinkedList()
    ll.prepend(1, 1)
    ll.prepend(2, 2)
    ll.prepend(3, 3)

    return ll


def test_move_to_front(linked_list):
    tail = linked_list.tail
    linked_list.move_to_front(tail)

    assert linked_list.head.data == tail.data
