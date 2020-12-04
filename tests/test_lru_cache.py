import pytest
from lru_cache import LruCache


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
    print(full_cache._location)
    full_cache.insert(4, 4)
    assert full_cache.get(1) == None


def test_get(full_cache):
    assert full_cache.get(1) == 1


def test_get_not_found(empty_cache):
    assert empty_cache.get(1) == None


def test_delete(empty_cache):
    empty_cache.insert(1, 1)
    empty_cache.delete(1)

    assert empty_cache.get(1) == None


def test_delete_not_found(empty_cache):
    empty_cache.delete(1)

    assert empty_cache.get(1) == None
