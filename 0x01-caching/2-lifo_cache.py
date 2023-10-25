#!/usr/bin/python3
"""
BaseCaching module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    Utilize LIFO method to implement caching
    """
    def __init__(self):
        super().__init__()
        self.history = []

    def put(self, key, item):
        """
        Include item in cache, hashing it with key
        """
        if not key or not item:
            pass
        else:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
                self.history.remove(key)
                self.history.append(key)
            elif len(self.cache_data) < BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item
                self.history.append(key)
            else:
                print(f'DISCARD: {self.history[-1]}')
                del self.cache_data[self.history[-1]]
                self.history.pop()
                self.cache_data[key] = item
                self.history.append(key)

    def get(self, key):
        """
        Gets cached data from memory using the given key
        """
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
