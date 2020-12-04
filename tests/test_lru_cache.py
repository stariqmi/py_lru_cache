from unittest.mock import patch
import pytest
from lru_cache import LruCache
from datastructures.linked_list import DoublyLinkedList


@pytest.fixture
def empty_cache():
    return LruCache(1)


@pytest.fixture
def full_cache():
    cache = LruCache(3)

    cache.insert(1, 1)
    cache.insert(2, 2)
    cache.insert(3, 3)

    return cache


def test_insert(empty_cache):
    empty_cache.insert(1, 1)
    assert empty_cache.get(1) == 1


def test_insert_with_eviction(full_cache):
    full_cache.insert(4, 4)
    assert full_cache.get(1) == None


def test_get(full_cache):
    assert full_cache.get(1) == 1


@patch.object(DoublyLinkedList, "move_to_front")
def test_get_moves_key_to_front(mock, full_cache):
    full_cache.get(1)
    mock.assert_called_once()


def test_get_not_found(empty_cache):
    assert empty_cache.get(1) == None


def test_delete(full_cache):
    full_cache.delete(2)

    assert full_cache.get(2) == None


def test_delete_not_found(empty_cache):
    empty_cache.delete(1)

    assert empty_cache.get(1) == None


def test_delete_most_recent_used(full_cache):
    full_cache.delete(3)

    assert full_cache.get(3) == None


def test_delete_least_recent_used(full_cache):
    full_cache.delete(1)

    assert full_cache.get(1) == None


def test_flush(full_cache):
    full_cache.flush()

    assert full_cache.get(1) == None
    assert full_cache.get(2) == None
    assert full_cache.get(3) == None


def test_flush_resets_doubly_linked_list(full_cache):
    old_doubly_linked_list = full_cache._doubly_linked_list
    full_cache.flush()

    assert full_cache._doubly_linked_list is not old_doubly_linked_list


def test_flush_resets_hash(full_cache):
    old_hash_map = full_cache._hash_map
    full_cache.flush()

    assert full_cache._hash_map is not old_hash_map
