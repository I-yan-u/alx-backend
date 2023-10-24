#!/usr/bin/python3
"""
BaseCaching module
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    Utilize FIFO method to implement caching
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Include item in cache, hashing it with key
        """
        if not key or not item:
            pass
        else:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
            elif len(self.cache_data) < BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item
            else:
                idx = [*self.cache_data.keys()]
                print(f'DISCARD: {idx[0]}')
                del self.cache_data[idx[0]]
                self.cache_data[key] = item

    def get(self, key):
        """
        Gets cached data from memory using the given key
        """
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
