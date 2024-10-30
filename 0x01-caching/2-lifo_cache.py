#!/usr/bin/env python3
"""
    Create a class LIFOCache that inherits
    from BaseCaching and is a caching system:
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """a lif0 caching class"""
    def __init__(self):
        """the initialization method"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ put an item in cache"""
        if key is None and item is None:
            return
        if key or item:
            if key not in self.cache_data:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    new_key = self.order.pop()
                    del self.cache_data[new_key]
                    print(f"DISCARD: {new_key}")
            else:
                self.order.remove(key)
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
            Must return the value in self.cache_data
            linked to key.
            If key is None or if the key doesn’t exist
            in self.cache_data, return None.
        """
        if key is None:
            return None

        if key not in self.cache_data:
            return None

        return self.cache_data.get(key)
