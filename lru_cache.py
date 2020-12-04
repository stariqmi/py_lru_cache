class LruCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache = {}

    def get(self, key):
        return self._cache.get(key)

    def insert(self, key, value):
        self._cache[key] = value
        return True

    def delete(self, key):
        del self._cache[key]
        return True
