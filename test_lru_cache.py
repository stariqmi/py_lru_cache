import pytest
from .lru_cache import LruCache


@pytest.fixture
def empty_cache():
    return LruCache(1)


def test_insert(empty_cache):
    assert empty_cache.insert(1, 1)


def test_get(empty_cache):
    key = 1
    value = 1

    empty_cache.insert(key, value)
    assert empty_cache.get(key) == value


def test_delete(empty_cache):
    empty_cache.insert(1, 1)
    assert empty_cache.delete(1)
