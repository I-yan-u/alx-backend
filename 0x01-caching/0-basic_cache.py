#!/usr/bin/python3
"""
BaseCaching module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Implements basic python dictionary caching
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Include item in cache hashing it with key
        """
        if not key or not item:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Gets cached data from memory using the given key
        """
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
