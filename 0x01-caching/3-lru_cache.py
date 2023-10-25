#!/usr/bin/python3
"""
BaseCaching module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.time_keeper = {}
        self.count = 0
        
    def put(self, key, item):
        if key is None or item is None:
            pass
        else:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
            elif len(self.cache_data) < BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item
                self.time_keeper[self.count] = key
                self.count += 1
            else:
                used_list = sorted(self.time_keeper.keys())
                print(f'DISCARD: {self.time_keeper[used_list[0]]}')
                del self.cache_data[self.time_keeper[used_list[0]]]
                del self.time_keeper[used_list[0]]
                self.cache_data[key] = item
                self.count += 1
                self.time_keeper[self.count] = key


    def get(self, key):
        """
        Gets cached data from memory using the given key
        """
        if not key or key not in self.cache_data.keys():
            return None
        self.count += 1
        for k, v in self.time_keeper.items():
            if key == v:
                del self.time_keeper[k]
                break
        self.time_keeper[self.count] = key
        return self.cache_data[key]
